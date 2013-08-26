# DCMS auto-generated file
# 2013-06-09 17:00:18.558000

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework.routers import DefaultRouter

from chronicle.views import ChronicleViewSet, GameViewSet

router = DefaultRouter()
router.register('Chronicle', ChronicleViewSet)
router.register('Game', GameViewSet)
