# DCMS auto-generated file
# Fri, 15 Nov 2013 07:37:00 -0600 | df9a64121d8facdb7d8b93b585110f26

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework import viewsets

from chronicle import models, serializers


class ChronicleViewSet (viewsets.ModelViewSet):
    model            = models.Chronicle
    serializer_class = serializers.ChronicleSerializer


class GameViewSet (viewsets.ModelViewSet):
    model            = models.Game
    serializer_class = serializers.GameSerializer


