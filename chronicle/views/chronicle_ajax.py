# DCMS auto-generated file
# 2013-09-10 11:58:03.321986

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework import viewsets

from chronicle.models import Chronicle, Game
from chronicle.serializers import ChronicleSerializer, GameSerializer


class ChronicleViewSet (viewsets.ModelViewSet):
    model            = Chronicle
    serializer_class = ChronicleSerializer


class GameViewSet (viewsets.ModelViewSet):
    model            = Game
    serializer_class = GameSerializer
