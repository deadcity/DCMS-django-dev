# DCMS auto-generated file
# 2013-09-23 10:18:14.789000

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import serializers

from traits.models import AttributeType, DerangementType, FlawType, MeritType, SkillType, Vice, Virtue, Affiliation, Attribute, CharacterText, CombatTrait, CreatureType, Derangement, Flaw, Genealogy, Merit, MiscTrait, Power, Skill, Subgroup


class AttributeTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = AttributeType
AttributeType.Serializer = AttributeTypeSerializer


class DerangementTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = DerangementType
DerangementType.Serializer = DerangementTypeSerializer


class FlawTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = FlawType
FlawType.Serializer = FlawTypeSerializer


class MeritTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = MeritType
MeritType.Serializer = MeritTypeSerializer


class SkillTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = SkillType
SkillType.Serializer = SkillTypeSerializer


class ViceSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Vice
Vice.Serializer = ViceSerializer


class VirtueSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Virtue
Virtue.Serializer = VirtueSerializer


class AffiliationSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Affiliation
Affiliation.Serializer = AffiliationSerializer


class AttributeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Attribute
Attribute.Serializer = AttributeSerializer


class CharacterTextSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterText
CharacterText.Serializer = CharacterTextSerializer


class CombatTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CombatTrait
CombatTrait.Serializer = CombatTraitSerializer


class CreatureTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CreatureType
CreatureType.Serializer = CreatureTypeSerializer


class DerangementSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Derangement
Derangement.Serializer = DerangementSerializer


class FlawSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Flaw
Flaw.Serializer = FlawSerializer


class GenealogySerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Genealogy
Genealogy.Serializer = GenealogySerializer


class MeritSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Merit
Merit.Serializer = MeritSerializer


class MiscTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = MiscTrait
MiscTrait.Serializer = MiscTraitSerializer


class PowerSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Power
Power.Serializer = PowerSerializer


class SkillSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Skill
Skill.Serializer = SkillSerializer


class SubgroupSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Subgroup
Subgroup.Serializer = SubgroupSerializer
