# DCMS auto-generated file
# Thu, 14 Nov 2013 17:01:01 -0600 | a7a72a7ad24bcd285a07fddad3149447

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from django.contrib import admin

from chronicle import models


class GameInline (admin.TabularInline):
    model = models.Game


