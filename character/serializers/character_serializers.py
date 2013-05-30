# DCMS auto-generated file
# 2013-05-24 10:08:14.612453

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import serializers

from character.models import Character


class CharacterSerializer (serializers.ModelSerializer):
    class Meta (object):
        model = Character
Character.Serializer = CharacterSerializer
