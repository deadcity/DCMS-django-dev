# DCMS auto-generated file
# Fri, 15 Nov 2013 07:37:00 -0600 | 9c52dd233ac3b342bc780ea6a841844d

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework import viewsets

from character import models, serializers


class CharacterViewSet (viewsets.ModelViewSet):
    model            = models.Character
    serializer_class = serializers.CharacterSerializer


class CharacterHasAttributeViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasAttribute
    serializer_class = serializers.CharacterHasAttributeSerializer


class CharacterHasCombatTraitViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasCombatTrait
    serializer_class = serializers.CharacterHasCombatTraitSerializer


class CharacterHasDerangementViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasDerangement
    serializer_class = serializers.CharacterHasDerangementSerializer


class CharacterHasFlawViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasFlaw
    serializer_class = serializers.CharacterHasFlawSerializer


class CharacterHasMeritViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasMerit
    serializer_class = serializers.CharacterHasMeritSerializer


class CharacterHasMiscTraitViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasMiscTrait
    serializer_class = serializers.CharacterHasMiscTraitSerializer


class CharacterHasPowerViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasPower
    serializer_class = serializers.CharacterHasPowerSerializer


class CharacterHasSkillViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasSkill
    serializer_class = serializers.CharacterHasSkillSerializer


class CharacterHasSkillSpecialtyViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasSkillSpecialty
    serializer_class = serializers.CharacterHasSkillSpecialtySerializer


class CharacterHasTextViewSet (viewsets.ModelViewSet):
    model            = models.CharacterHasText
    serializer_class = serializers.CharacterHasTextSerializer


