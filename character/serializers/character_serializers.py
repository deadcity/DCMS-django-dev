# DCMS auto-generated file
# 2013-05-30 12:10:52.781713

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import serializers

from character.models import Character, CharacterHasAttribute, CharacterHasCombatTrait, CharacterHasDerangement, CharacterHasFlaw, CharacterHasMerit, CharacterHasMiscTrait, CharacterHasPower, CharacterHasSkill, CharacterHasSkillSpecialty, CharacterHasText


class CharacterSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Character
Character.Serializer = CharacterSerializer


class CharacterHasAttributeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasAttribute
CharacterHasAttribute.Serializer = CharacterHasAttributeSerializer


class CharacterHasCombatTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasCombatTrait
CharacterHasCombatTrait.Serializer = CharacterHasCombatTraitSerializer


class CharacterHasDerangementSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasDerangement
CharacterHasDerangement.Serializer = CharacterHasDerangementSerializer


class CharacterHasFlawSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasFlaw
CharacterHasFlaw.Serializer = CharacterHasFlawSerializer


class CharacterHasMeritSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasMerit
CharacterHasMerit.Serializer = CharacterHasMeritSerializer


class CharacterHasMiscTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasMiscTrait
CharacterHasMiscTrait.Serializer = CharacterHasMiscTraitSerializer


class CharacterHasPowerSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasPower
CharacterHasPower.Serializer = CharacterHasPowerSerializer


class CharacterHasSkillSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasSkill
CharacterHasSkill.Serializer = CharacterHasSkillSerializer


class CharacterHasSkillSpecialtySerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasSkillSpecialty
CharacterHasSkillSpecialty.Serializer = CharacterHasSkillSpecialtySerializer


class CharacterHasTextSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasText
CharacterHasText.Serializer = CharacterHasTextSerializer
