from rest_framework import serializers

from traits.models import AttributeType, Attribute, SkillType, Skill


class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AttributeType


class AttributeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Attribute


class SkillTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = SkillType


class SkillSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Skill
