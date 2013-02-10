from rest_framework import serializers

from common.generators import generate_serializer
import character


for model in character.models._character_trait_models:
    globals()[model._meta.object_name + 'Serializer'] = generate_serializer(model)


class CharacterSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = character.models.Character
