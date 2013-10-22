# DCMS auto-generated file
# Wed, 23 Oct 2013 07:49:46 -0500 | eed898c5fcd988363bbb5c37c131a006

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework import serializers

from traits import models




class AttributeTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.AttributeType
models.AttributeType.Serializer = AttributeTypeSerializer



class DerangementTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.DerangementType
models.DerangementType.Serializer = DerangementTypeSerializer



class FlawTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.FlawType
models.FlawType.Serializer = FlawTypeSerializer



class MeritTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.MeritType
models.MeritType.Serializer = MeritTypeSerializer



class SkillTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.SkillType
models.SkillType.Serializer = SkillTypeSerializer



class StatusSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Status
models.Status.Serializer = StatusSerializer



class ViceSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Vice
models.Vice.Serializer = ViceSerializer



class VirtueSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Virtue
models.Virtue.Serializer = VirtueSerializer



class AffiliationSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Affiliation
models.Affiliation.Serializer = AffiliationSerializer



class AttributeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Attribute
models.Attribute.Serializer = AttributeSerializer



class CharacterTextSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterText
models.CharacterText.Serializer = CharacterTextSerializer



class CombatTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CombatTrait
models.CombatTrait.Serializer = CombatTraitSerializer



class CreatureTypeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CreatureType
models.CreatureType.Serializer = CreatureTypeSerializer



class DerangementSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Derangement
models.Derangement.Serializer = DerangementSerializer



class FlawSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Flaw
models.Flaw.Serializer = FlawSerializer



class GenealogySerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Genealogy
models.Genealogy.Serializer = GenealogySerializer



class MeritSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Merit
models.Merit.Serializer = MeritSerializer



class MiscTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.MiscTrait
models.MiscTrait.Serializer = MiscTraitSerializer



class PowerSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Power
models.Power.Serializer = PowerSerializer



class SkillSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Skill
models.Skill.Serializer = SkillSerializer



class SubgroupSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Subgroup
models.Subgroup.Serializer = SubgroupSerializer




