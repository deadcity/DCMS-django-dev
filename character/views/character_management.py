from django.shortcuts import render
from django.shortcuts import redirect
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
    Subgroup
)
import traits.serializers

def is_storyteller(user):
    if user.is_authenticated:
        if user.groups.filter(id=1).exists():
            return True
    return False

def add_character_enums_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['vices']   = Vice   .objects.filter(**kwargs)
    context['virtues'] = Virtue .objects.filter(**kwargs)

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


def character_list (request):
    user = request.user
    if is_storyteller(user):
        context = {
            'character_list' : [{
                'character'   : character,
                'can_submit'  : True,
                'can_edit'    : True,
                'can_disable' : True,
            } for character in Character.objects.all()]
        }
    else:
        context = {
            'character_list' : [{
                'character'   : character,
                'can_submit'  : True,
                'can_edit'    : True,
                'can_disable' : True,
            } for character in Character.objects.filter(user=user)]
        }
    add_character_enums_to_context(context)
    add_summary_data_to_context(context)

    return render(request, 'character/character_list.html', context)


def character_edit (request, pk):
    user = request.user
    context = {
        'character': Character.objects.get(pk = pk),
    }
    if (context['character'].user != user) and not is_storyteller(user):
        redirect('/characters')

    add_character_enums_to_context(context)
    add_summary_data_to_context(context)
    add_trait_enums_to_context(context)
    add_trait_data_to_context(context)
    add_charcter_data_to_context(context, character__id = pk)

    return render(request, 'character/character_edit.html', context)


class CharacterDetailView (generic.DetailView):
    model = Character
    template_name = 'character/character_detail.html'
