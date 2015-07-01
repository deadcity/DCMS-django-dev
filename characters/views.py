## @module characters.views
#  Provides view functions and classes related to character management.


from datetime import datetime
from itertools import chain
from json import loads  # DEBUG

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from characters.models import Character
from dsqla.models import ModelEncoder
from dsqla.session import session
from traits.models import (
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

    character_has_traits = set(chain(
        character.attributes,
        character.skills,
    ))

    traits = set(cht.trait for cht in character_has_traits)
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
            character_has_traits
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

    # TODO(Emery): This needs to actually go through the chronicle's access
    #              rules and build up the list of trait availabilities.  For
    #              now, just return everything.

    return JsonResponse(
        {
            'CreatureType' : { 'ALLOW' : list(session.query(CreatureType)), },
            'Genealogy'    : { 'ALLOW' : list(session.query(Genealogy)),    },
            'Affiliation'  : { 'ALLOW' : list(session.query(Affiliation)),  },
            'Subgroup'     : { 'ALLOW' : list(session.query(Subgroup)),     },
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

    # print('REQUEST:', request.body.decode('ascii'))
    key, value = request.body.decode('ascii').split('=')
    setattr(character, key, value)

    # TODO(Emery): This needs to go through the access rules that are dependent
    #              on the character-summary traits that changed and see if any
    #              traits have changed access permissions.
    return JsonResponse(
        {},
        encoder = ModelEncoder
    )
