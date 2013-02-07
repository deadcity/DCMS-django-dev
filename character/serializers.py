from rest_framework import serializers

import character


def _create_serializer(model):
    Meta = type(
        'Meta',
        (object,),
        dict(model = model)
    )
    return type(
        model._meta.object_name + 'Serializer',
        (serializers.ModelSerializer,),
        dict(Meta = Meta)
    )

for model in character.models._character_trait_models:
    globals()[model._meta.object_name + 'Serializer'] = _create_serializer(model)


class CharacterSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = character.models.Character
