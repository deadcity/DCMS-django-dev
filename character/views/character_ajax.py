# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import generics

from character.models import Character
from character.serializers import CharacterSerializer


class CharacterDetail (generics.RetrieveUpdateDestroyAPIView):
    model            = Character
    serializer_class = CharacterSerializer

class CharacterList (generics.ListCreateAPIView):
    model            = Character
    serializer_class = CharacterSerializer
