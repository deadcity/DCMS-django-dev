# DCMS auto-generated file
# Thu, 14 Nov 2013 16:50:28 -0600 | e3a5e7df24371f8b2d2a89b945b5acc2

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from django.contrib import admin

from chronicle import models


class ChronicleAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'description',)
    list_filter  = ('enabled', 'description',)
admin.site.register(models.Chronicle, ChronicleAdmin)


class GameAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'chronicle', 'date',)
    list_filter  = ('enabled', 'chronicle', 'date',)
admin.site.register(models.Game, GameAdmin)


