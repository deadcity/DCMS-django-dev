# DCMS auto-generated file
# Fri, 15 Nov 2013 07:34:34 -0600 | b94734211d8eb0777a0301e35bb0032b

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework.routers import DefaultRouter

from chronicle import views


router = DefaultRouter()

router.register('Chronicle', views.ChronicleViewSet)
router.register('Game', views.GameViewSet)


