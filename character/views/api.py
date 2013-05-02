from django.db.models.loading import get_model
from django.shortcuts import render

from rest_framework import generics

import character.models as models
import character.serializers as serializers
from common.generators import APIDetail_Metaclass, APIList_Metaclass


# # # # # # #
# API Views #
# # # # # # #

# Detail Views

class CharacterDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = models.Character
    serializer_class = serializers.CharacterSerializer

class CharacterHasAttributeDetail      : __metaclass__ = APIDetail_Metaclass(models.CharacterHasAttribute,      serializers.CharacterHasAttribute)
class CharacterHasCombatTraitDetail    : __metaclass__ = APIDetail_Metaclass(models.CharacterHasCombatTrait,    serializers.CharacterHasCombatTrait)
class CharacterHasDerangementDetail    : __metaclass__ = APIDetail_Metaclass(models.CharacterHasDerangement,    serializers.CharacterHasDerangement)
class CharacterHasFlawDetail           : __metaclass__ = APIDetail_Metaclass(models.CharacterHasFlaw,           serializers.CharacterHasFlaw)
class CharacterHasMeritDetail          : __metaclass__ = APIDetail_Metaclass(models.CharacterHasMerit,          serializers.CharacterHasMerit)
class CharacterHasMiscTraitDetail      : __metaclass__ = APIDetail_Metaclass(models.CharacterHasMiscTrait,      serializers.CharacterHasMiscTrait)
class CharacterHasPowerDetail          : __metaclass__ = APIDetail_Metaclass(models.CharacterHasPower,          serializers.CharacterHasPower)
class CharacterHasSkillDetail          : __metaclass__ = APIDetail_Metaclass(models.CharacterHasSkill,          serializers.CharacterHasSkill)
class CharacterHasSkillSpecialtyDetail : __metaclass__ = APIDetail_Metaclass(models.CharacterHasSkillSpecialty, serializers.CharacterHasSkillSpecialty)
class CharacterHasTextDetail           : __metaclass__ = APIDetail_Metaclass(models.CharacterHasText,           serializers.CharacterHasText)
class CharacterHasTraitDetail          : __metaclass__ = APIDetail_Metaclass(models.CharacterHasTrait,          serializers.CharacterHasTrait)

# List Views

class CharacterList (generics.ListCreateAPIView):
    model            = models.Character
    serializer_class = serializers.CharacterSerializer

class CharacterHasAttributeList      : __metaclass__ = APIList_Metaclass(models.CharacterHasAttribute,      serializers.CharacterHasAttribute)
class CharacterHasCombatTraitList    : __metaclass__ = APIList_Metaclass(models.CharacterHasCombatTrait,    serializers.CharacterHasCombatTrait)
class CharacterHasDerangementList    : __metaclass__ = APIList_Metaclass(models.CharacterHasDerangement,    serializers.CharacterHasDerangement)
class CharacterHasFlawList           : __metaclass__ = APIList_Metaclass(models.CharacterHasFlaw,           serializers.CharacterHasFlaw)
class CharacterHasMeritList          : __metaclass__ = APIList_Metaclass(models.CharacterHasMerit,          serializers.CharacterHasMerit)
class CharacterHasMiscTraitList      : __metaclass__ = APIList_Metaclass(models.CharacterHasMiscTrait,      serializers.CharacterHasMiscTrait)
class CharacterHasPowerList          : __metaclass__ = APIList_Metaclass(models.CharacterHasPower,          serializers.CharacterHasPower)
class CharacterHasSkillList          : __metaclass__ = APIList_Metaclass(models.CharacterHasSkill,          serializers.CharacterHasSkill)
class CharacterHasSkillSpecialtyList : __metaclass__ = APIList_Metaclass(models.CharacterHasSkillSpecialty, serializers.CharacterHasSkillSpecialty)
class CharacterHasTextList           : __metaclass__ = APIList_Metaclass(models.CharacterHasText,           serializers.CharacterHasText)
class CharacterHasTraitList          : __metaclass__ = APIList_Metaclass(models.CharacterHasTrait,          serializers.CharacterHasTrait)


# # # # # # # # # # # # # # # #
# Generate BackboneJS models  #
# # # # # # # # # # # # # # # #

def generate_character_trait_model (request, character_trait_name):
    Model = get_model('character', character_trait_name)
    return render(request, 'character/character_trait_model.js', {
        'model_name' : Model._meta.object_name,
        'Model'      : Model,
    }, content_type = 'text/javascript')
