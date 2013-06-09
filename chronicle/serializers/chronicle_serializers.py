# DCMS auto-generated file
# 2013-06-09 17:00:18.558000

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import serializers

from chronicle.models import Chronicle, Game


class ChronicleSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Chronicle
Chronicle.Serializer = ChronicleSerializer


class GameSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Game
Game.Serializer = GameSerializer
