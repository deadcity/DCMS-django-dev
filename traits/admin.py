from django.contrib import admin
from traits.models import (
    AttributeType,      Attribute,
    CombatTrait,
    DerangementType,    Derangement,
    MeritFlawType,      Flaw,
    SkillType,          Skill
)


class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(AttributeType, AttributeTypeAdmin)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Attribute, AttributeAdmin)


class CombatTraitAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter  = ('enabled',)
admin.site.register(CombatTrait, CombatTraitAdmin)


class DerangementTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(DerangementType, DerangementTypeAdmin)

class DerangementAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type', 'requires_specification',)
    list_filter  = ('enabled', 'type', 'requires_specification',)
admin.site.register(Derangement, DerangementAdmin)


class MeritFlawTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(MeritFlawType)

class FlawAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Flaw, FlawAdmin)


class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(SkillType, SkillTypeAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Skill, SkillAdmin)
