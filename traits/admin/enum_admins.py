# DCMS auto-generated file
# Wed, 23 Oct 2013 18:19:49 -0500 | b764b94aed43a40970e4c0e0596bf1e8

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from django.contrib import admin

from traits import models




class AttributeTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.AttributeType, AttributeTypeAdmin)



class DerangementTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.DerangementType, DerangementTypeAdmin)



class FlawTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.FlawType, FlawTypeAdmin)



class MeritTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.MeritType, MeritTypeAdmin)



class SkillTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.SkillType, SkillTypeAdmin)



class ViceAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.Vice, ViceAdmin)



class VirtueAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.Virtue, VirtueAdmin)




