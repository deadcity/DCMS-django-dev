from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import generic

from rest_framework.renderers import JSONRenderer

from character.models import Character
from character.models import (
    CharacterHasAttribute,
    CharacterHasCombatTrait,
    CharacterHasDerangement,
    CharacterHasFlaw,
    CharacterHasMerit,
    CharacterHasMiscTrait,
    CharacterHasPower,
    CharacterHasSkill,
    CharacterHasSkillSpecialty,
    CharacterHasText,
    CharacterHasTrait
)
import character.serializers
from traits.models import (
    AttributeType,
    DerangementType,
    FlawType,
    MeritType,
    SkillType,
    Status,
    Vice,
    Virtue
)
from traits.models import (
    Affiliation,
    Attribute,
    CharacterText,
    CombatTrait,
    CreatureType,
    Derangement,
    Flaw,
    Genealogy,
    Merit,
    MiscTrait,
    Power,
    Skill,
    Status,
    Subgroup
)
import traits.serializers


def is_storyteller(user):
    if user.groups.filter(id=1).exists():
        return True
    return False


def add_character_enums_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['statuses'] = Status .objects.filter(**kwargs)
    context['vices']    = Vice   .objects.filter(**kwargs)
    context['virtues']  = Virtue .objects.filter(**kwargs)

    return context


def add_summary_data_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['affiliations']   = Affiliation  .objects.filter(**kwargs)
    context['creature_types'] = CreatureType .objects.filter(**kwargs)
    context['genealogies']    = Genealogy    .objects.filter(**kwargs)
    context['subgroups']      = Subgroup     .objects.filter(**kwargs)

    return context


def add_trait_enums_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['attribute_types']   = AttributeType   .objects.filter(**kwargs)
    context['derangement_types'] = DerangementType .objects.filter(**kwargs)
    context['flaw_types']        = FlawType        .objects.filter(**kwargs)
    context['merit_types']       = MeritType       .objects.filter(**kwargs)
    context['skill_types']       = SkillType       .objects.filter(**kwargs)

    return context


def add_trait_data_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['attributes']      = Attribute     .objects.filter(**kwargs)
    context['character_texts'] = CharacterText .objects.filter(**kwargs)
    context['combat_traits']   = CombatTrait   .objects.filter(**kwargs)
    context['derangements']    = Derangement   .objects.filter(**kwargs)
    context['flaws']           = Flaw          .objects.filter(**kwargs)
    context['merits']          = Merit         .objects.filter(**kwargs)
    context['misc_traits']     = MiscTrait     .objects.filter(**kwargs)
    context['powers']          = Power         .objects.filter(**kwargs)
    context['skills']          = Skill         .objects.filter(**kwargs)

    return context


def add_charcter_data_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['character_has_attribute']       = CharacterHasAttribute      .objects.filter(**kwargs)
    context['character_has_combat_trait']    = CharacterHasCombatTrait    .objects.filter(**kwargs)
    context['character_has_derangement']     = CharacterHasDerangement    .objects.filter(**kwargs)
    context['character_has_flaw']            = CharacterHasFlaw           .objects.filter(**kwargs)
    context['character_has_merit']           = CharacterHasMerit          .objects.filter(**kwargs)
    context['character_has_misc_trait']      = CharacterHasMiscTrait      .objects.filter(**kwargs)
    context['character_has_power']           = CharacterHasPower          .objects.filter(**kwargs)
    context['character_has_skill']           = CharacterHasSkill          .objects.filter(**kwargs)
    context['character_has_skill_specialty'] = CharacterHasSkillSpecialty .objects.filter(**kwargs)
    context['character_has_text']            = CharacterHasText           .objects.filter(**kwargs)

    return context


def add_character_text_to_context (user, context = None, **kwargs):
    if not context:
        context = {}

    if is_storyteller(user):
        context['character_has_text'] = CharacterHasText.objects.filter(**kwargs)
    else:
        context['character_has_text'] = CharacterHasText.objects.filter(trait__hide_from_player = False, **kwargs)

    return context


@login_required
def character_list (request):
    user = request.user
    status_editing = Status.objects.get(name = 'Editing')
    if is_storyteller(user):
        context = {
            'character_list' : [{
                'character'   : character,
                'can_submit'  : character.status == status_editing,
                'can_edit'    : True,
                'can_disable' : True,
            } for character in Character.objects.all()],
            'is_storyteller' : True
        }
    else:
        context = {
            'character_list' : [{
                'character'   : character,
                'can_submit'  : character.status == status_editing,
                'can_edit'    : character.status == status_editing,
                'can_disable' : character.status == status_editing,
            } for character in Character.objects.filter(user=user.id)],
            'is_storyteller' : False
        }
    add_character_enums_to_context(context)
    add_summary_data_to_context(context)

    return render(request, 'character/character_list.html', context)


@login_required
def print_all (request):
    if not is_storyteller(request.user):
        redirect('/characters')

    context = { 'character_list': Character.objects.filter(status = 4) }

    return render(request, 'character/print_all.html', context)


@login_required
def new_character (request):
    character = Character(
        user = request.user,
        status = Status.objects.get(name = 'Editing'),
        creature_type = CreatureType.objects.get(name = 'Vampire'),
        # TODO(emery): have these default to values like "(not selected)" instead.
        genealogy = Genealogy.objects.get(name = 'Daeva'),
        affiliation = Affiliation.objects.get(name = 'Carthian Movement'),
        # subgroup
        virtue = Virtue.objects.get(name = 'Charity'),
        vice = Vice.objects.get(name = 'Envy')
    )
    character.save()

    for trait in Attribute.objects.all():
        CharacterHasAttribute(character = character, trait = trait).save()

    for trait in Skill.objects.all():
        CharacterHasSkill(character = character, trait = trait).save()

    for trait in CombatTrait.objects.all():
        CharacterHasCombatTrait(character = character, trait = trait).save()

    for trait in MiscTrait.objects.filter(enabled = True):
        CharacterHasMiscTrait(character = character, trait = trait).save()

    for trait in CharacterText.objects.filter(enabled = True):
        CharacterHasText(character = character, trait = trait).save()

    return redirect('character_edit', pk = character.pk)


@login_required
def character_edit (request, pk):
    user = request.user
    context = {
        'character': Character.objects.get(pk = pk),
        'is_storyteller': is_storyteller(user)
    }
    if (context['character'].user != user or context['character'].status != Status.objects.get(name = 'Editing')) and not is_storyteller(user):
        return redirect('character_list')

    add_character_enums_to_context(context)
    add_summary_data_to_context(context)
    add_trait_enums_to_context(context)
    add_trait_data_to_context(context)
    add_charcter_data_to_context(context, character__id = pk)
    add_character_text_to_context(user, context, character__id = pk)

    return render(request, 'character/character_edit.html', context)


@login_required
def submit_character (request, pk):
    user = request.user
    character = Character.objects.get(pk = pk)
    if character.user != user:
        messages.error(request, "You cannot submit a character that isn't yours.")
    elif character.status != Status.objects.get(name = 'Editing'):
        messages.error(request, "Character \"{}\" has already been submitted.".format(character.name))
    else:
        character.status = Status.objects.get(name = 'Submitted')
        character.date_submitted = datetime.now()
        character.save()
        messages.success(request, "Character \"{}\" has been submitted.".format(character.name))
    return redirect('character_list')


class CharacterDetailView (generic.DetailView):
    model = Character
    template_name = 'character/character_detail.html'


def character_detail (request, pk):
    user = request.user
    context = {
        'character': Character.objects.get(pk = pk),
        'is_storyteller': is_storyteller(user)
    }
    if (context['character'].user != user) and not is_storyteller(user):
        return redirect('character_list')

    return render(request, 'character/character_detail.html', context)
