# DCMS auto-generated file
# 2013-09-10 11:58:03.321986

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import viewsets

from traits.models import AttributeType, DerangementType, FlawType, MeritType, SkillType, Status, Vice, Virtue, Affiliation, Attribute, CharacterText, CombatTrait, CreatureType, Derangement, Flaw, Genealogy, Merit, MiscTrait, Power, Skill, Subgroup
from traits.serializers import AttributeTypeSerializer, DerangementTypeSerializer, FlawTypeSerializer, MeritTypeSerializer, SkillTypeSerializer, StatusSerializer, ViceSerializer, VirtueSerializer, AffiliationSerializer, AttributeSerializer, CharacterTextSerializer, CombatTraitSerializer, CreatureTypeSerializer, DerangementSerializer, FlawSerializer, GenealogySerializer, MeritSerializer, MiscTraitSerializer, PowerSerializer, SkillSerializer, SubgroupSerializer


class AttributeTypeViewSet (viewsets.ModelViewSet):
    model            = AttributeType
    serializer_class = AttributeTypeSerializer


class DerangementTypeViewSet (viewsets.ModelViewSet):
    model            = DerangementType
    serializer_class = DerangementTypeSerializer


class FlawTypeViewSet (viewsets.ModelViewSet):
    model            = FlawType
    serializer_class = FlawTypeSerializer


class MeritTypeViewSet (viewsets.ModelViewSet):
    model            = MeritType
    serializer_class = MeritTypeSerializer


class SkillTypeViewSet (viewsets.ModelViewSet):
    model            = SkillType
    serializer_class = SkillTypeSerializer


class StatusViewSet (viewsets.ModelViewSet):
    model            = Status
    serializer_class = StatusSerializer


class ViceViewSet (viewsets.ModelViewSet):
    model            = Vice
    serializer_class = ViceSerializer


class VirtueViewSet (viewsets.ModelViewSet):
    model            = Virtue
    serializer_class = VirtueSerializer


class AffiliationViewSet (viewsets.ModelViewSet):
    model            = Affiliation
    serializer_class = AffiliationSerializer


class AttributeViewSet (viewsets.ModelViewSet):
    model            = Attribute
    serializer_class = AttributeSerializer


class CharacterTextViewSet (viewsets.ModelViewSet):
    model            = CharacterText
    serializer_class = CharacterTextSerializer


class CombatTraitViewSet (viewsets.ModelViewSet):
    model            = CombatTrait
    serializer_class = CombatTraitSerializer


class CreatureTypeViewSet (viewsets.ModelViewSet):
    model            = CreatureType
    serializer_class = CreatureTypeSerializer


class DerangementViewSet (viewsets.ModelViewSet):
    model            = Derangement
    serializer_class = DerangementSerializer


class FlawViewSet (viewsets.ModelViewSet):
    model            = Flaw
    serializer_class = FlawSerializer


class GenealogyViewSet (viewsets.ModelViewSet):
    model            = Genealogy
    serializer_class = GenealogySerializer


class MeritViewSet (viewsets.ModelViewSet):
    model            = Merit
    serializer_class = MeritSerializer


class MiscTraitViewSet (viewsets.ModelViewSet):
    model            = MiscTrait
    serializer_class = MiscTraitSerializer


class PowerViewSet (viewsets.ModelViewSet):
    model            = Power
    serializer_class = PowerSerializer


class SkillViewSet (viewsets.ModelViewSet):
    model            = Skill
    serializer_class = SkillSerializer


class SubgroupViewSet (viewsets.ModelViewSet):
    model            = Subgroup
    serializer_class = SubgroupSerializer
