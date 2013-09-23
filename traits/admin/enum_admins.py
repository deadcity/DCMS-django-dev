# DCMS auto-generated file
# 2013-09-23 10:18:14.789000

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.contrib import admin

from traits.models import AttributeType, DerangementType, FlawType, MeritType, SkillType, Vice, Virtue


class AttributeTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(AttributeType, AttributeTypeAdmin)

class DerangementTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(DerangementType, DerangementTypeAdmin)

class FlawTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(FlawType, FlawTypeAdmin)

class MeritTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(MeritType, MeritTypeAdmin)

class SkillTypeAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(SkillType, SkillTypeAdmin)

class ViceAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Vice, ViceAdmin)

class VirtueAdmin (admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Virtue, VirtueAdmin)
