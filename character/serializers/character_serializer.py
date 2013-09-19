from rest_framework import serializers

from character.models import Character


class CharacterSerializer (serializers.ModelSerializer):
    playername = serializers.CharField(source = 'user.first_name', read_only = True)

    class Meta (object):
        model = Character
Character.Serializer = CharacterSerializer

