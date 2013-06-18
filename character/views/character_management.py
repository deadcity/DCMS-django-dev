from django.shortcuts import render
from django.views import generic

from rest_framework.renderers import JSONRenderer

from character.models import Character
from traits.models import AttributeType, DerangementType, FlawType, MeritType, SkillType, Vice, Virtue
from traits.models import Affiliation, CreatureType, Genealogy, Subgroup
from traits.models import Attribute, CharacterText, CombatTrait, Derangement, Flaw, Merit, MiscTrait, Power, Skill
import traits.serializers


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



def character_list (request):
    context = {
        'character_list' : [{
            'character'   : character,
            'can_submit'  : True,
            'can_edit'    : True,
            'can_disable' : True,
        } for character in Character.objects.all()]
    }
    add_character_enums_to_context(context)
    add_summary_data_to_context(context)

    return render(request, 'character/character_list.html', context)


class CharacterDetailView (generic.DetailView):
    model = Character
    template_name = 'character/character_detail.html'
