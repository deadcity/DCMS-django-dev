# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import generics

from character.models import CharacterHasAttribute, CharacterHasCombatTrait, CharacterHasDerangement, CharacterHasFlaw, CharacterHasMerit, CharacterHasMiscTrait, CharacterHasPower, CharacterHasSkill, CharacterHasSkillSpecialty, CharacterHasText
from character.serializers import CharacterHasAttributeSerializer, CharacterHasCombatTraitSerializer, CharacterHasDerangementSerializer, CharacterHasFlawSerializer, CharacterHasMeritSerializer, CharacterHasMiscTraitSerializer, CharacterHasPowerSerializer, CharacterHasSkillSerializer, CharacterHasSkillSpecialtySerializer, CharacterHasTextSerializer


class CharacterHasAttributeDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasAttribute
    serializer_class = CharacterHasAttributeSerializer

class CharacterHasAttributeList (generics.ListCreateAPIView):
    model            = CharacterHasAttribute
    serializer_class = CharacterHasAttributeSerializer


class CharacterHasCombatTraitDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasCombatTrait
    serializer_class = CharacterHasCombatTraitSerializer

class CharacterHasCombatTraitList (generics.ListCreateAPIView):
    model            = CharacterHasCombatTrait
    serializer_class = CharacterHasCombatTraitSerializer


class CharacterHasDerangementDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasDerangement
    serializer_class = CharacterHasDerangementSerializer

class CharacterHasDerangementList (generics.ListCreateAPIView):
    model            = CharacterHasDerangement
    serializer_class = CharacterHasDerangementSerializer


class CharacterHasFlawDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasFlaw
    serializer_class = CharacterHasFlawSerializer

class CharacterHasFlawList (generics.ListCreateAPIView):
    model            = CharacterHasFlaw
    serializer_class = CharacterHasFlawSerializer


class CharacterHasMeritDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasMerit
    serializer_class = CharacterHasMeritSerializer

class CharacterHasMeritList (generics.ListCreateAPIView):
    model            = CharacterHasMerit
    serializer_class = CharacterHasMeritSerializer


class CharacterHasMiscTraitDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasMiscTrait
    serializer_class = CharacterHasMiscTraitSerializer

class CharacterHasMiscTraitList (generics.ListCreateAPIView):
    model            = CharacterHasMiscTrait
    serializer_class = CharacterHasMiscTraitSerializer


class CharacterHasPowerDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasPower
    serializer_class = CharacterHasPowerSerializer

class CharacterHasPowerList (generics.ListCreateAPIView):
    model            = CharacterHasPower
    serializer_class = CharacterHasPowerSerializer


class CharacterHasSkillDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasSkill
    serializer_class = CharacterHasSkillSerializer

class CharacterHasSkillList (generics.ListCreateAPIView):
    model            = CharacterHasSkill
    serializer_class = CharacterHasSkillSerializer


class CharacterHasSkillSpecialtyDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasSkillSpecialty
    serializer_class = CharacterHasSkillSpecialtySerializer

class CharacterHasSkillSpecialtyList (generics.ListCreateAPIView):
    model            = CharacterHasSkillSpecialty
    serializer_class = CharacterHasSkillSpecialtySerializer


class CharacterHasTextDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = CharacterHasText
    serializer_class = CharacterHasTextSerializer

class CharacterHasTextList (generics.ListCreateAPIView):
    model            = CharacterHasText
    serializer_class = CharacterHasTextSerializer
