from rest_framework import generics

from traits.models import AttributeType, Attribute
from traits.serializers import AttributeTypeSerializer, AttributeSerializer


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
