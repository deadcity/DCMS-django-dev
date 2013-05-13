# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import serializers

from character.models import CharacterHasAttribute, CharacterHasCombatTrait, CharacterHasDerangement, CharacterHasFlaw, CharacterHasMerit, CharacterHasMiscTrait, CharacterHasPower, CharacterHasSkill, CharacterHasSkillSpecialty, CharacterHasText


class CharacterHasAttributeSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasAttribute


class CharacterHasCombatTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasCombatTrait


class CharacterHasDerangementSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasDerangement


class CharacterHasFlawSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasFlaw


class CharacterHasMeritSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasMerit


class CharacterHasMiscTraitSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasMiscTrait


class CharacterHasPowerSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasPower


class CharacterHasSkillSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasSkill


class CharacterHasSkillSpecialtySerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasSkillSpecialty


class CharacterHasTextSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = CharacterHasText
