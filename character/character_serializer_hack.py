# This file is a hack to get around our lacking of a client-side User model.
# Delete this file when we do implement a client-side User model.

from rest_framework import serializers

from character.models import Character


class CharacterSerializerHack (serializers.ModelSerializer):
    playername = serializers.CharField(source = 'user.first_name', read_only = True)

    class Meta (object):
        model = Character
Character.Serializer = CharacterSerializerHack
