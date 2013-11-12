# DCMS auto-generated file
# Tue, 12 Nov 2013 07:44:40 -0600 | 2cb9f60359dadf8cef5e822aae69a6ad

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




