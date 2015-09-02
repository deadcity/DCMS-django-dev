## @module characters.views
#  Provides view functions and classes related to character management.


from sys import stdout

from collections import defaultdict
from datetime import datetime
from itertools import chain
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import View

from characters.models import Character, CharacterTrait
from dsqla.models import get_referenced_model, ModelEncoder
from dsqla.session import session
from dsqla.view_mixins import JsonBody
from trait_access.models import (
    AccessRule, calculate_availabilities,
    CharacterHasTrait, CharacterDoesNotHaveTrait
)
from traits.models import (
    Trait,
    AttributeType, SkillType, MeritType, FlawType,
    CreatureType, Genealogy, Affiliation, Subgroup
)


class HttpResponseUnauthorized (HttpResponse):
    status_code = 401


def storyteller_or_owner (request, character, action, **response_kwargs):
    # TODO(Emery): check if user has storyteller permissions on this character

    if character.user_id != request.user.id:
        return HttpResponseUnauthorized(
            "Must be the character's owner or storyteller to {}.".format(action),
            **response_kwargs
        )


def storyteller_or_editing_owner (request, character, action, **response_kwargs):
    # TODO(Emery): check if user has storyteller permissions on this character

    if character.user_id != request.user.id:
        return HttpResponseUnauthorized(
            "Must be the character's owner or storyteller to {}.".format(action),
            **response_kwargs
        )

    if character.status != Character.Status.EDITING:
        return HttpResponseForbidden(
            "Character must have a status of 'EDITING' to {}.".format(action),
            **response_kwargs
        )

    return None


@login_required
def character_list (request):
    characters = session.query(Character)

    return render(request, 'characters/character_list.html', {
        'characters': characters,
        'records': chain(
            set(character.creature_type for character in characters),
            set(character.genealogy     for character in characters),
            set(character.affiliation   for character in characters),
            set(character.subgroup      for character in characters),
        ),
    })


@login_required
def show_character (request, id):
    character = session.query(Character).get(int(id))

    response = storyteller_or_owner(request, character, 'view')
    if response:
        return response

    return render(request, 'characters/show_character.html', {
        'character': character,
    })


@login_required
def edit_character (request, id):
    character = session.query(Character).get(int(id))

    response = storyteller_or_editing_owner(request, character, 'edit')
    if response:
        return response

    character_traits = set(chain(
        character.attributes,
        character.skills,
        character.skill_specialties,
        character.powers,
    ))

    traits = set(chain(
        (char_power.trait.power_group for char_power in character.powers),
        (cht.trait for cht in character_traits),
    ))
    if character.creature_type : traits.add(character.creature_type)
    if character.genealogy     : traits.add(character.genealogy)
    if character.affiliation   : traits.add(character.affiliation)
    if character.subgroup      : traits.add(character.subgroup)

    return render(request, 'characters/character_edit.html', {
        'character': character,
        'models': list(chain(
            [character.user, character.chronicle],
            session.query(AttributeType),
            session.query(SkillType),
            traits,
            character_traits
        )),
    })


@login_required
@require_http_methods(['PUT'])
def submit_character (request, id):
    character = session.query(Character).get(int(id))

    # Must own the character to submit it.
    if character.user_id != request.user.id:
        return HttpResponseUnauthorized(
            "Must be the character's owner to submit.",
            content_type = 'application/json'
        )

    # Character must be in 'EDITING' mode to submit it.
    if character.status != Character.Status.EDITING:
        return HttpResponseForbidden(
            "Character must have a status of 'EDITING' to submit.",
            content_type = 'application/json'
        )

    character.status = Character.Status.SUBMITTED
    character.date_submitted = datetime.now()

    return JsonResponse(
        character.to_dict(),
        safe = False,
        encoder = ModelEncoder
    )


@login_required
@require_http_methods(['PUT'])
def disable_character (request, id):
    character = session.query(Character).get(int(id))

    if character.enabled is False:
        return HttpResponseForbidden(
            'Character already disabled.',
            content_type = 'application/json'
        )

    response = storyteller_or_editing_owner(request, character, 'disable',
        content_type = 'application/json')
    if response:
        return response

    character.enabled = False

    return JsonResponse(
        character.to_dict(),
        safe = False,
        encoder = ModelEncoder
    )


@login_required
@require_http_methods(['PUT'])
def enable_character (request, id):
    character = session.query(Character).get(int(id))

    if character.enabled is False:
        return HttpResponseForbidden(
            'Character already enabled.',
            content_type = 'application/json'
        )

    response = storyteller_or_editing_owner(request, character, 'enable',
        content_type = 'application/json')
    if response:
        return response

    character.enabled = True

    return JsonResponse(
        character.to_dict(),
        safe = False,
        encoder = ModelEncoder
    )


@login_required
def available_traits (request, id):
    character = session.query(Character).get(int(id))

    response = storyteller_or_editing_owner(request, character, 'edit')
    if response:
        return response

    chronicle_ids = [c.id for c in character.chronicle.all_chronicles]
    availabilities = calculate_availabilities(
        character,
        session.query(Trait).filter(
            Trait.chronicle_id.in_(chronicle_ids)
        )
    )

    return JsonResponse(
        {
            'availabilities': availabilities,
        },
        encoder = ModelEncoder
    )


@login_required
@require_http_methods(['PATCH'])
def update_character_summary (request, id):
    character = session.query(Character).get(int(id))

    response = storyteller_or_editing_owner(request, character, 'edit')
    if response:
        return response

    chronicle_ids = [c.id for c in character.chronicle.all_chronicles]
    affected_traits = set()
    data = json.loads(request.body.decode('ascii'))

    for key, value in data.items():
        column = Character.__table__.columns[key]

        if len(column.foreign_keys) == 0:
            old_value = getattr(character, key)
            new_value = value

            # TODO (Emery): Check rules for character_summary attributes. (Name, last_edited, ...)

        else:
            TraitType = get_referenced_model(column)

            key = key[:-3]  # assumes key in format "<key>_id"
            old_value = getattr(character, key)
            new_value = None if value is None else session.query(TraitType).get(value)

            if old_value:
                changing_trait_ids = (old_value.id,)
            else:
                changing_trait_ids = tuple()
            if new_value:
                changing_trait_ids += (new_value.id,)

            # Rule: character-has-trait
            for rule in session.query(CharacterHasTrait).filter(
                CharacterHasTrait.chronicle_id.in_(chronicle_ids),
                CharacterHasTrait.other_trait_id.in_(changing_trait_ids)
            ):
                affected_traits.add(rule.trait)

            # Rule: character-does-not-have-trait
            for rule in session.query(CharacterDoesNotHaveTrait).filter(
                CharacterDoesNotHaveTrait.chronicle_id.in_(chronicle_ids),
                CharacterDoesNotHaveTrait.other_trait_id.in_(changing_trait_ids)
            ):
                affected_traits.add(rule.trait)

        # Set attribute on character.
        setattr(character, key, new_value)

    session.flush()

    # Recalculate availabilities for affected traits.
    availabilities = calculate_availabilities(character, affected_traits)

    return JsonResponse(
        {
            'character': character,
            'availabilities': availabilities,
        },
        encoder = ModelEncoder
    )


class CharacterTraitView (JsonBody, View):
    @method_decorator(login_required)
    def dispatch (self, request, id, character_trait_id, *args, **kwargs):
        self._id = int(id)

        response = storyteller_or_editing_owner(request, self.character,
            'edit character-trait')
        if response:
            return response

        return super().dispatch(request, character_trait_id, *args, **kwargs)

    @property
    def character (self):
        if hasattr(self, '_character') and self._character and self._character.id is self._id:
            return self._character
        character = session.query(Character).get(self._id)
        self._character = character
        return character

    def recalculate_access (self, trait):
        affected_traits = set()
        chronicle_ids = [c.id for c in self.character.chronicle.all_chronicles]

        # Rule: character-has-trait
        for rule in session.query(CharacterHasTrait).filter(
            CharacterHasTrait.chronicle_id.in_(chronicle_ids),
            CharacterHasTrait.other_trait_id == trait.id
        ):
            affected_traits.add(rule.trait)

        # Rule: character-does-not-have-trait
        for rule in session.query(CharacterDoesNotHaveTrait).filter(
            CharacterDoesNotHaveTrait.chronicle_id.in_(chronicle_ids),
            CharacterDoesNotHaveTrait.other_trait_id == trait.id
        ):
            affected_traits.add(rule.trait)

        # Recalculate availabilities for affected traits.
        availabilities = calculate_availabilities(self.character, affected_traits)

        return availabilities

    # CRUD: create
    def post (self, request, character_trait_id):
        polymorphic_on = CharacterTrait.__mapper__.polymorphic_on
        polymorphic_value = request.data[polymorphic_on.name]
        mapper = CharacterTrait.__mapper__.polymorphic_map[polymorphic_value]
        Model = mapper.class_
        self.character.date_last_edited = datetime.now()

        # Create the new character trait and commit the addition so that the
        # model gets assigned an id.
        character_trait = Model(**request.data)
        session.add(character_trait)
        session.commit()
        trait = character_trait.trait

        return JsonResponse(
            {
                'character': self.character,
                'model': character_trait,
                'availabilities': self.recalculate_access(trait),
            },
            encoder = ModelEncoder
        )

    # CRUD: update
    def patch (self, request, character_trait_id):
        character_trait = session.query(CharacterTrait).get(character_trait_id)
        trait = character_trait.trait
        for field, value in request.data.items():
            setattr(character_trait, field, value)
        self.character.date_last_edited = datetime.now()
        session.commit()

        return JsonResponse(
            {
                'character': self.character,
                'model': character_trait,
                'availabilities': self.recalculate_access(trait),
            },
            encoder = ModelEncoder
        )

    # CRUD: delete
    def delete (self, request, character_trait_id):
        character_trait = session.query(CharacterTrait).get(character_trait_id)
        trait = character_trait.trait
        self.character.date_last_edited = datetime.now()
        character_trait_attrs = character_trait.to_dict()

        # Delete the model and commit the change so that the deletion propagates
        # to any relationship collections that might reference this model.
        session.delete(character_trait)
        session.commit()

        return JsonResponse(
            {
                'character': self.character,
                'model': character_trait_attrs,
                'availabilities': self.recalculate_access(trait),
            },
            encoder = ModelEncoder
        )
