# DCMS auto-generated file
# Thu, 7 Nov 2013 07:49:55 -0600 | 615154420ae00815e107a429686901d6

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




