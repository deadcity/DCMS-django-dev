# DCMS auto-generated file
# Fri, 15 Nov 2013 07:32:07 -0600 | 29060f221ccdcf5f55316ccb27dd5036

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework import serializers

from chronicle import models


class ChronicleSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Chronicle
models.Chronicle.Serializer = ChronicleSerializer


class GameSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.Game
models.Game.Serializer = GameSerializer


