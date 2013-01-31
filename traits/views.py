from rest_framework import generics

from traits.models import (
    AttributeType, Attribute,
    SkillType,     Skill
)
from traits.serializers import (
    AttributeTypeSerializer, AttributeSerializer,
    SkillTypeSerializer,     SkillSerializer
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
