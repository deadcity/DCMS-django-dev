# DCMS auto-generated file
# Thu, 7 Nov 2013 07:49:55 -0600 | 0c9d317c43a8116ff7ebf6fb9632d7d4

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




