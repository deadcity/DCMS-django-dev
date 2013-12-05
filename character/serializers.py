# DCMS auto-generated file
# Thu, 5 Dec 2013 08:39:39 -0600 | 9f4c207e1870f20202041ecbc57a1220

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework import serializers

from character import models


class CharacterSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Character
models.Character.Serializer = CharacterSerializer


class XPRecordSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.XPRecord
models.XPRecord.Serializer = XPRecordSerializer


class CharacterHasAttributeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasAttribute
models.CharacterHasAttribute.Serializer = CharacterHasAttributeSerializer


class CharacterHasCombatTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasCombatTrait
models.CharacterHasCombatTrait.Serializer = CharacterHasCombatTraitSerializer


class CharacterHasDerangementSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasDerangement
models.CharacterHasDerangement.Serializer = CharacterHasDerangementSerializer


class CharacterHasFlawSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasFlaw
models.CharacterHasFlaw.Serializer = CharacterHasFlawSerializer


class CharacterHasMeritSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasMerit
models.CharacterHasMerit.Serializer = CharacterHasMeritSerializer


class CharacterHasMiscTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasMiscTrait
models.CharacterHasMiscTrait.Serializer = CharacterHasMiscTraitSerializer


class CharacterHasPowerSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasPower
models.CharacterHasPower.Serializer = CharacterHasPowerSerializer


class CharacterHasSkillSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasSkill
models.CharacterHasSkill.Serializer = CharacterHasSkillSerializer


class CharacterHasSkillSpecialtySerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasSkillSpecialty
models.CharacterHasSkillSpecialty.Serializer = CharacterHasSkillSpecialtySerializer


class CharacterHasTextSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.CharacterHasText
models.CharacterHasText.Serializer = CharacterHasTextSerializer

