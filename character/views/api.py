from rest_framework import generics

import character
import character.serializers as character_serializers
from common.generators import generate_api_list, generate_api_detail


for Model in character.models._character_trait_models:
    model_name  = Model._meta.object_name
    Serializer  = getattr(character_serializers, model_name + 'Serializer')
    list_name   = model_name + 'List'
    detail_name = model_name + 'Detail'
    globals()[list_name]   = generate_api_list  (list_name,   Model, Serializer)
    globals()[detail_name] = generate_api_detail(detail_name, Model, Serializer)


class CharacterList(generics.ListCreateAPIView):
    model            = character.models.Character
    serializer_class = character.serializers.CharacterSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = character.models.Character
    serializer_class = character.serializers.CharacterSerializer
