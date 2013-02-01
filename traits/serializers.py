from rest_framework import serializers

from traits.models import (
    AttributeType,      Attribute,
    CombatTrait,
    DerangementType,    Derangement,
    MeritFlawType,      Flaw,
    SkillType,          Skill,
)


class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AttributeType

class AttributeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Attribute


class CombatTraitSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CombatTrait


class DerangementTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = DerangementType

class DerangementSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Derangement


class MeritFlawTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = MeritFlawType

class FlawSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Flaw


class SkillTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = SkillType

class SkillSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Skill
