from rest_framework import serializers

import traits.models as trait_models

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


class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AttributeType

class DerangementTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = DerangementType

class FlawTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = FlawType

class SkillTypeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = SkillType



class AttributeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Attribute

class CombatTraitSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CombatTrait

class DerangementSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Derangement

class FlawSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Flaw

class SkillSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Skill
