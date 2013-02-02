from rest_framework import generics

from traits.models import (
    AttributeType,
    DerangementType,
    FlawType,
    SkillType,

    Attribute,
    CombatTrait,
    Derangement,
    Flaw,
    Skill,
)
from traits.serializers import (
    AttributeTypeSerializer,
    DerangementTypeSerializer,
    FlawTypeSerializer,
    SkillTypeSerializer,

    AttributeSerializer,
    CombatTraitSerializer,
    DerangementSerializer,
    FlawSerializer,
    SkillSerializer,
)


class AttributeTypeList(generics.ListCreateAPIView):
    model            = AttributeType
    serializer_class = AttributeTypeSerializer

class AttributeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = AttributeType
    serializer_class = AttributeTypeSerializer


class DerangementTypeList(generics.ListCreateAPIView):
    model            = DerangementType
    serializer_class = DerangementTypeSerializer

class DerangementTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = DerangementType
    serializer_class = DerangementTypeSerializer


class FlawTypeList(generics.ListCreateAPIView):
    model            = FlawType
    serializer_class = FlawTypeSerializer

class FlawTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = FlawType
    serializer_class = FlawTypeSerializer


class SkillTypeList(generics.ListCreateAPIView):
    model            = SkillType
    serializer_class = SkillTypeSerializer

class SkillTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = SkillType
    serializer_class = SkillTypeSerializer




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


class DerangementList(generics.ListCreateAPIView):
    model            = Derangement
    serializer_class = DerangementSerializer

class DerangementDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = Derangement
    serializer_class = DerangementSerializer


class FlawList(generics.ListCreateAPIView):
    model            = Flaw
    serializer_class = FlawSerializer

class FlawDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = Flaw
    serializer_class = FlawSerializer


class SkillList(generics.ListCreateAPIView):
    model            = Skill
    serializer_class = SkillSerializer

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = Skill
    serializer_class = SkillSerializer
