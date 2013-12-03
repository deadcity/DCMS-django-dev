from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect

from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from character import models as character_models
from character.permissions import character_permissions, character_trait_permissions, is_storyteller
import character.serializers
from common.routers import action, link, list_action
from traits import models as trait_models
import traits.serializers


def add_character_enums_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['statuses'] = character_models.CharacterStatus._elements
    context['vices']    = trait_models.Vice   .objects.filter(**kwargs)
    context['virtues']  = trait_models.Virtue .objects.filter(**kwargs)

    return context


def add_summary_data_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['affiliations']   = trait_models.Affiliation  .objects.filter(**kwargs)
    context['creature_types'] = trait_models.CreatureType .objects.filter(**kwargs)
    context['genealogies']    = trait_models.Genealogy    .objects.filter(**kwargs)
    context['subgroups']      = trait_models.Subgroup     .objects.filter(**kwargs)

    return context


def add_trait_enums_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['attribute_types']   = trait_models.AttributeType   .objects.filter(**kwargs)
    context['derangement_types'] = trait_models.DerangementType .objects.filter(**kwargs)
    context['flaw_types']        = trait_models.FlawType        .objects.filter(**kwargs)
    context['merit_types']       = trait_models.MeritType       .objects.filter(**kwargs)
    context['skill_types']       = trait_models.SkillType       .objects.filter(**kwargs)

    return context


def add_trait_data_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['attributes']      = trait_models.Attribute     .objects.filter(**kwargs)
    context['character_texts'] = trait_models.CharacterText .objects.filter(**kwargs)
    context['combat_traits']   = trait_models.CombatTrait   .objects.filter(**kwargs)
    context['derangements']    = trait_models.Derangement   .objects.filter(**kwargs)
    context['flaws']           = trait_models.Flaw          .objects.filter(**kwargs)
    context['merits']          = trait_models.Merit         .objects.filter(**kwargs)
    context['misc_traits']     = trait_models.MiscTrait     .objects.filter(**kwargs)
    context['powers']          = trait_models.Power         .objects.filter(**kwargs)
    context['skills']          = trait_models.Skill         .objects.filter(**kwargs)

    return context


def add_character_data_to_context (context = None, **kwargs):
    if not context:
        context = {}

    context['character_has_attribute']       = character_models.CharacterHasAttribute      .objects.filter(**kwargs)
    context['character_has_combat_trait']    = character_models.CharacterHasCombatTrait    .objects.filter(**kwargs)
    context['character_has_derangement']     = character_models.CharacterHasDerangement    .objects.filter(**kwargs)
    context['character_has_flaw']            = character_models.CharacterHasFlaw           .objects.filter(**kwargs)
    context['character_has_merit']           = character_models.CharacterHasMerit          .objects.filter(**kwargs)
    context['character_has_misc_trait']      = character_models.CharacterHasMiscTrait      .objects.filter(**kwargs)
    context['character_has_power']           = character_models.CharacterHasPower          .objects.filter(**kwargs)
    context['character_has_skill']           = character_models.CharacterHasSkill          .objects.filter(**kwargs)
    context['character_has_skill_specialty'] = character_models.CharacterHasSkillSpecialty .objects.filter(**kwargs)
    context['character_has_text']            = character_models.CharacterHasText           .objects.filter(**kwargs)

    return context


def add_character_text_to_context(user, context = None, **kwargs):
    if not context:
        context = {}

    if is_storyteller(user):
        context['character_has_text'] = character_models.CharacterHasText.objects.filter(**kwargs)
    else:
        context['character_has_text'] = character_models.CharacterHasText.objects.filter(trait__hide_from_player = False, **kwargs)

    return context


class CharacterManagementViewSet (viewsets.ModelViewSet):
    model              = character_models.Character
    serializer_class   = character_models.Character.Serializer
    renderer_classes   = (TemplateHTMLRenderer, JSONRenderer)
    permission_classes = character_permissions

    def get_queryset (self):
        if is_storyteller(self.request.user):
            return self.model.objects.all()
        return self.model.objects.filter(user = self.request.user)

    def list (self, request):
        queryset = self.get_queryset()

        if request.accepted_renderer.format == 'html':
            user = request.user
            status_EDITING = character_models.CharacterStatus.EDITING

            if is_storyteller(user):
                context = {
                    'character_list' : [{
                        'character'   : character,
                        'can_submit'  : character.status == status_EDITING,
                        'can_edit'    : True,
                        'can_disable' : True,
                    } for character in queryset],
                    'is_storyteller' : True
                }
            else:
                context = {
                    'character_list' : [{
                        'character'   : character,
                        'can_submit'  : character.status == status_EDITING,
                        'can_edit'    : character.status == status_EDITING,
                        'can_disable' : character.status == status_EDITING,
                    } for character in queryset],
                    'is_storyteller' : False
                }

            add_character_enums_to_context(context)
            add_summary_data_to_context(context)

            return Response(context, template_name = 'character/character_list.html')

        else:
            serializer = self.get_serializer(queryset, many = True)
            return Response(serializer.data)

    def retrieve (self, request, pk):
        user = request.user
        is_st = is_storyteller(user)
        character = self.get_object()

        if request.accepted_renderer.format == 'html':
            return Response({
                'character': self.model.objects.get(pk = pk),
                'is_storyteller': is_storyteller(user)
            }, template_name = 'character/character_detail.html')

        else:
            serializer = self.get_serializer(character)
            return Response(serializer.data)

    @list_action(name = 'new')
    def create_new_character (self, request):
        character = self.model(
            user = request.user,
            status = character_models.CharacterStatus.EDITING,
            creature_type = trait_models.CreatureType.objects.get(name = 'Vampire')
        )
        character.save()

        for trait in trait_models.Attribute.objects.all():
            character_models.CharacterHasAttribute(character = character, trait = trait).save()

        for trait in trait_models.Skill.objects.all():
            character_models.CharacterHasSkill(character = character, trait = trait).save()

        for trait in trait_models.CombatTrait.objects.all():
            character_models.CharacterHasCombatTrait(character = character, trait = trait).save()

        for trait in trait_models.MiscTrait.objects.all():
            character_models.CharacterHasMiscTrait(character = character, trait = trait).save()

        for trait in trait_models.CharacterText.objects.all():
            character_models.CharacterHasText(character = character, trait = trait).save()

        # TODO(emery): Find some way to redirect instead.
        return self.edit(self.request, pk = character.pk)

    @link()
    def edit (self, request, pk):
        user = request.user
        is_st = is_storyteller(user)
        character = self.get_object()

        if not is_st and character.status != character_models.CharacterStatus.EDITING:
            return Response(template_name = 'character/not_editable.html')

        context = {
            'character': character,
            'is_storyteller': is_st,
        }

        add_character_enums_to_context(context)
        add_summary_data_to_context(context)
        add_trait_enums_to_context(context)
        add_trait_data_to_context(context)
        add_character_data_to_context(context, character__id = pk)
        add_character_text_to_context(user, context, character__id = pk)

        return Response(context, template_name = 'character/character_edit.html')

    @action()
    def submit (self, request, pk):
        user = request.user
        character = self.get_object()
        if character.user != request.user:
            messages.error(request, "You cannot submit a character that isn't yours.")
        elif character.status != character_models.CharacterStatus.EDITING:
            messages.error(request, 'Character "{}" has already been submitted.'.format(character.name))
        else:
            character.status = character_models.CharacterStatus.SUBMITTED
            character.date_submitted = datetime.now()
            character.save()
            messages.success(request, 'Character "{}" has been submitted.'.format(character.name))
        return self.list(request)


class CharacterViewSet (viewsets.ModelViewSet):
    model              = character_models.Character
    serializer_class   = model.Serializer
    permission_classes = character_permissions


class CharacterHasAttributeViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasAttribute
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasCombatTraitViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasCombatTrait
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasDerangementViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasDerangement
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasFlawViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasFlaw
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasMeritViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasMerit
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasMiscTraitViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasMiscTrait
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasPowerViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasPower
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasSkillViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasSkill
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasSkillSpecialtyViewSet (viewsets.ModelViewSet):
    model              = character_models.CharacterHasSkillSpecialty
    serializer_class   = model.Serializer
    permission_classes = character_trait_permissions


class CharacterHasTextViewSet   (viewsets.ModelViewSet):
    permission_classes = character_trait_permissions
    model            = character_models.CharacterHasText
    serializer_class = model.Serializer
