from django.contrib import admin
from traits.models import AttributeType, Attribute, SkillType, Skill


class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(AttributeType, AttributeTypeAdmin)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Attribute, AttributeAdmin)

class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(SkillType, SkillTypeAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Skill, SkillAdmin)
