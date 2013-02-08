from rest_framework import generics

import character


def _create_api_list(model, model_name):
    return type(
        model_name + 'List',
        (generics.ListCreateAPIView,),
        dict(
            model            = model,
            serializer_class = getattr(character.serializer, model_name + 'Serializer')
        )
    )

def _create_api_detail(model, model_name):
    return type(
        model_name + 'Detail',
        (generics.RetrieveUpdateDestroyAPIView,),
        dict(
            model            = model,
            serializer_class = getattr(character.Serializer, model_name + 'Serializer')
        )
    )

for model in character._character_trait_models:
    model_name = model._meta.object_name
    globals()[model_name + 'List']   = _create_api_list  (model, model_name)
    globals()[model_name + 'Detail'] = _create_api_detail(model, model_name)


class CharacterList(generics.ListCreateAPIView):
    model            = character.models.Character
    serializer_class = character.serializers.CharacterSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    model            = character.models.Character
    serializer_class = character.serializers.CharacterSerializer
