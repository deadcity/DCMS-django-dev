from django.contrib import admin
from traits.models import (
    AttributeType,
    DerangementType,
    FlawType,
    SkillType,

    Attribute,
    CombatTrait,
    Derangement,
    Flaw,
    Skill
)


class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(AttributeType, AttributeTypeAdmin)

class DerangementTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(DerangementType, DerangementTypeAdmin)

class FlawTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(FlawType)

class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(SkillType, SkillTypeAdmin)


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Attribute, AttributeAdmin)

class CombatTraitAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter  = ('enabled',)
admin.site.register(CombatTrait, CombatTraitAdmin)

class DerangementAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type', 'requires_specification',)
    list_filter  = ('enabled', 'type', 'requires_specification',)
admin.site.register(Derangement, DerangementAdmin)

class FlawAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Flaw, FlawAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Skill, SkillAdmin)
