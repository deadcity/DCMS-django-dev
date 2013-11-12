# DCMS auto-generated file
# Thu, 7 Nov 2013 07:51:59 -0600 | bac879d0f2956e3570004be1000e1dae

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




