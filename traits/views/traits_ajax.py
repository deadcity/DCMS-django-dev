# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import generics

from traits.models import AttributeType, DerangementType, FlawType, MeritType, SkillType, Vice, Virtue, Affiliation, Attribute, CharacterText, CombatTrait, CreatureType, Derangement, Flaw, Genealogy, Merit, MiscTrait, Power, Skill, Subgroup
from traits.serializers import AttributeTypeSerializer, DerangementTypeSerializer, FlawTypeSerializer, MeritTypeSerializer, SkillTypeSerializer, ViceSerializer, VirtueSerializer, AffiliationSerializer, AttributeSerializer, CharacterTextSerializer, CombatTraitSerializer, CreatureTypeSerializer, DerangementSerializer, FlawSerializer, GenealogySerializer, MeritSerializer, MiscTraitSerializer, PowerSerializer, SkillSerializer, SubgroupSerializer


class AttributeTypeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = AttributeType
    serializer_class = AttributeTypeSerializer

class AttributeTypeList (generics.ListCreateAPIView):
    model            = AttributeType
    serializer_class = AttributeTypeSerializer


class DerangementTypeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = DerangementType
    serializer_class = DerangementTypeSerializer

class DerangementTypeList (generics.ListCreateAPIView):
    model            = DerangementType
    serializer_class = DerangementTypeSerializer


class FlawTypeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = FlawType
    serializer_class = FlawTypeSerializer

class FlawTypeList (generics.ListCreateAPIView):
    model            = FlawType
    serializer_class = FlawTypeSerializer


class MeritTypeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = MeritType
    serializer_class = MeritTypeSerializer

class MeritTypeList (generics.ListCreateAPIView):
    model            = MeritType
    serializer_class = MeritTypeSerializer


class SkillTypeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = SkillType
    serializer_class = SkillTypeSerializer

class SkillTypeList (generics.ListCreateAPIView):
    model            = SkillType
    serializer_class = SkillTypeSerializer


class ViceDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Vice
    serializer_class = ViceSerializer

class ViceList (generics.ListCreateAPIView):
    model            = Vice
    serializer_class = ViceSerializer


class VirtueDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Virtue
    serializer_class = VirtueSerializer

class VirtueList (generics.ListCreateAPIView):
    model            = Virtue
    serializer_class = VirtueSerializer


class AffiliationDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Affiliation
    serializer_class = AffiliationSerializer

class AffiliationList (generics.ListCreateAPIView):
    model            = Affiliation
    serializer_class = AffiliationSerializer


class AttributeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Attribute
    serializer_class = AttributeSerializer

class AttributeList (generics.ListCreateAPIView):
    model            = Attribute
    serializer_class = AttributeSerializer


class CharacterTextDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterText
    serializer_class = CharacterTextSerializer

class CharacterTextList (generics.ListCreateAPIView):
    model            = CharacterText
    serializer_class = CharacterTextSerializer


class CombatTraitDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CombatTrait
    serializer_class = CombatTraitSerializer

class CombatTraitList (generics.ListCreateAPIView):
    model            = CombatTrait
    serializer_class = CombatTraitSerializer


class CreatureTypeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CreatureType
    serializer_class = CreatureTypeSerializer

class CreatureTypeList (generics.ListCreateAPIView):
    model            = CreatureType
    serializer_class = CreatureTypeSerializer


class DerangementDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Derangement
    serializer_class = DerangementSerializer

class DerangementList (generics.ListCreateAPIView):
    model            = Derangement
    serializer_class = DerangementSerializer


class FlawDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Flaw
    serializer_class = FlawSerializer

class FlawList (generics.ListCreateAPIView):
    model            = Flaw
    serializer_class = FlawSerializer


class GenealogyDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Genealogy
    serializer_class = GenealogySerializer

class GenealogyList (generics.ListCreateAPIView):
    model            = Genealogy
    serializer_class = GenealogySerializer


class MeritDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Merit
    serializer_class = MeritSerializer

class MeritList (generics.ListCreateAPIView):
    model            = Merit
    serializer_class = MeritSerializer


class MiscTraitDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = MiscTrait
    serializer_class = MiscTraitSerializer

class MiscTraitList (generics.ListCreateAPIView):
    model            = MiscTrait
    serializer_class = MiscTraitSerializer


class PowerDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Power
    serializer_class = PowerSerializer

class PowerList (generics.ListCreateAPIView):
    model            = Power
    serializer_class = PowerSerializer


class SkillDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Skill
    serializer_class = SkillSerializer

class SkillList (generics.ListCreateAPIView):
    model            = Skill
    serializer_class = SkillSerializer


class SubgroupDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Subgroup
    serializer_class = SubgroupSerializer

class SubgroupList (generics.ListCreateAPIView):
    model            = Subgroup
    serializer_class = SubgroupSerializer
