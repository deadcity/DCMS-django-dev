# DCMS auto-generated file
# 2013-05-30 12:10:52.781713

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import viewsets

from character.models import Character, CharacterHasAttribute, CharacterHasCombatTrait, CharacterHasDerangement, CharacterHasFlaw, CharacterHasMerit, CharacterHasMiscTrait, CharacterHasPower, CharacterHasSkill, CharacterHasSkillSpecialty, CharacterHasText
from character.serializers import CharacterSerializer, CharacterHasAttributeSerializer, CharacterHasCombatTraitSerializer, CharacterHasDerangementSerializer, CharacterHasFlawSerializer, CharacterHasMeritSerializer, CharacterHasMiscTraitSerializer, CharacterHasPowerSerializer, CharacterHasSkillSerializer, CharacterHasSkillSpecialtySerializer, CharacterHasTextSerializer


class CharacterViewSet (viewsets.ModelViewSet):
    model            = Character
    serializer_class = CharacterSerializer


class CharacterHasAttributeViewSet (viewsets.ModelViewSet):
    model            = CharacterHasAttribute
    serializer_class = CharacterHasAttributeSerializer


class CharacterHasCombatTraitViewSet (viewsets.ModelViewSet):
    model            = CharacterHasCombatTrait
    serializer_class = CharacterHasCombatTraitSerializer


class CharacterHasDerangementViewSet (viewsets.ModelViewSet):
    model            = CharacterHasDerangement
    serializer_class = CharacterHasDerangementSerializer


class CharacterHasFlawViewSet (viewsets.ModelViewSet):
    model            = CharacterHasFlaw
    serializer_class = CharacterHasFlawSerializer


class CharacterHasMeritViewSet (viewsets.ModelViewSet):
    model            = CharacterHasMerit
    serializer_class = CharacterHasMeritSerializer


class CharacterHasMiscTraitViewSet (viewsets.ModelViewSet):
    model            = CharacterHasMiscTrait
    serializer_class = CharacterHasMiscTraitSerializer


class CharacterHasPowerViewSet (viewsets.ModelViewSet):
    model            = CharacterHasPower
    serializer_class = CharacterHasPowerSerializer


class CharacterHasSkillViewSet (viewsets.ModelViewSet):
    model            = CharacterHasSkill
    serializer_class = CharacterHasSkillSerializer


class CharacterHasSkillSpecialtyViewSet (viewsets.ModelViewSet):
    model            = CharacterHasSkillSpecialty
    serializer_class = CharacterHasSkillSpecialtySerializer


class CharacterHasTextViewSet (viewsets.ModelViewSet):
    model            = CharacterHasText
    serializer_class = CharacterHasTextSerializer
