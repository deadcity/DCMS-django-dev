# DCMS auto-generated file
# 2013-09-10 11:58:03.321986

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.contrib import admin

from chronicle.models import Game


class GameInline (admin.TabularInline):
    model = Game
