from rest_framework import serializers

from traits.models import AttributeType, Attribute


class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AttributeType


class AttributeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Attribute
