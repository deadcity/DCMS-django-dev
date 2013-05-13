# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

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


class DerangementTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = DerangementType


class FlawTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = FlawType


class MeritTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = MeritType


class SkillTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = SkillType


class ViceSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Vice


class VirtueSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Virtue


class AffiliationSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Affiliation


class AttributeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Attribute


class CharacterTextSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterText


class CombatTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CombatTrait


class CreatureTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CreatureType


class DerangementSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Derangement


class FlawSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Flaw


class GenealogySerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Genealogy


class MeritSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Merit


class MiscTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = MiscTrait


class PowerSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Power


class SkillSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Skill


class SubgroupSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Subgroup
