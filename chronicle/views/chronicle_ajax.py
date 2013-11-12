# DCMS auto-generated file
# Thu, 7 Nov 2013 07:49:55 -0600 | 6d37c862cbc127704918eb2a41d90ee1

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




