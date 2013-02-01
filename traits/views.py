from rest_framework import generics

from traits.models import (
    AttributeType,      Attribute,
    CombatTrait,
    DerangementType,    Derangment,
    MeritFlawType,      Flaw,
    SkillType,          Skill,
)
from traits.serializers import (
    AttributeTypeSerializer,    AttributeSerializer,
    CombatTraitSerializer,
    DerangementTypeSerializer,  DerangmentSerializer,
    MeritFlawTypeSerializer,    FlawSerializer,
    SkillTypeSerializer,        SkillSerializer,
)


class AttributeTypeList(generics.ListCreateAPIView):
    model            = AttributeType
    serializer_class = AttributeTypeSerializer

class AttributeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = AttributeType
    serializer_class = AttributeTypeSerializer


class AttributeList(generics.ListCreateAPIView):
    model            = Attribute
    serializer_class = AttributeSerializer

class AttributeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = Attribute
    serializer_class = AttributeSerializer


class CombatTraitList(generics.ListCreateAPIView):
    model            = CombatTrait
    serializer_class = CombatTraitSerializer

class CombatTraitDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = CombatTrait
    serializer_class = CombatTraitSerializer


class DerangementTypeList(generics.ListCreateAPIView):
    model            = DerangementType
    serializer_class = DerangementTypeSerializer

class DerangementTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = DerangementType
    serializer_class = DerangementTypeSerializer


class DerangmentList(generics.ListCreateAPIView):
    model            = Derangment
    serializer_class = DerangmentSerializer

class DerangmentDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = Derangment
    serializer_class = DerangmentSerializer


class MeritFlawTypeList(generics.ListCreateAPIView):
    model            = MeritFlawType
    serializer_class = MeritFlawTypeSerializer

class MeritFlawTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = MeritFlawType
    serializer_class = MeritFlawTypeSerializer


class FlawList(generics.ListCreateAPIView):
    model            = Flaw
    serializer_class = FlawSerializer

class FlawDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = Flaw
    serializer_class = FlawSerializer


class SkillTypeList(generics.ListCreateAPIView):
    model            = SkillType
    serializer_class = SkillTypeSerializer

class SkillTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = SkillType
    serializer_class = SkillTypeSerializer


class SkillList(generics.ListCreateAPIView):
    model            = Skill
    serializer_class = SkillSerializer

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = Skill
    serializer_class = SkillSerializer
