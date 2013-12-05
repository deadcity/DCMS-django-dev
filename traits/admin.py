from django.contrib import admin

from common.admin import make_admin_link
from traits import models


class EnumAdmin (admin.ModelAdmin):
    list_display = ('name',)


class AttributeTypeAdmin   (EnumAdmin): pass
class DerangementTypeAdmin (EnumAdmin): pass
class FlawTypeAdmin        (EnumAdmin): pass
class MeritTypeAdmin       (EnumAdmin): pass
class SkillTypeAdmin       (EnumAdmin): pass
class ViceAdmin            (EnumAdmin): pass
class VirtueAdmin          (EnumAdmin): pass

admin.site.register(models.AttributeType,   AttributeTypeAdmin)
admin.site.register(models.DerangementType, DerangementTypeAdmin)
admin.site.register(models.FlawType,        FlawTypeAdmin)
admin.site.register(models.MeritType,       MeritTypeAdmin)
admin.site.register(models.SkillType,       SkillTypeAdmin)
admin.site.register(models.Vice,            ViceAdmin)
admin.site.register(models.Virtue,          VirtueAdmin)


class AffiliationAdmin (admin.ModelAdmin):
    list_display  = ('name', 'enabled')
    list_filter   = ('enabled',)
    ordering      = ('name',)
    search_fields = ('name',)
admin.site.register(models.Affiliation, AffiliationAdmin)


class AttributeAdmin (admin.ModelAdmin):
    type_link     = make_admin_link(models.AttributeType, 'type')
    list_display  = ('name', 'enabled', 'type_link')
    list_filter   = ('enabled', 'type')
    ordering      = ('type', 'name')
    search_fields = ('name', 'type__name')
admin.site.register(models.Attribute, AttributeAdmin)


class CharacterTextAdmin (admin.ModelAdmin):
    list_display  = ('name', 'enabled', 'hide_from_player')
    list_filter   = ('enabled', 'hide_from_player')
    ordering      = ('name',)
    search_fields = ('name',)
admin.site.register(models.CharacterText, CharacterTextAdmin)


class CombatTraitAdmin (admin.ModelAdmin):
    list_display  = ('name', 'enabled')
    list_filter   = ('enabled',)
    ordering      = ('name',)
    search_fields = ('name',)
admin.site.register(models.CombatTrait, CombatTraitAdmin)


class CreatureTypeAdmin (admin.ModelAdmin):
    list_display  = ('name', 'enabled', 'genealogy_name', 'affiliation_name', 'subgroup_name', 'power_name')
    list_filter   = ('enabled',)
    ordering      = ('name',)
    search_fields = ('name', 'genealogy_name', 'affiliation_name', 'subgroup_name', 'power_name')
admin.site.register(models.CreatureType, CreatureTypeAdmin)


class DerangementAdmin (admin.ModelAdmin):
    type_link     = make_admin_link(models.DerangementType, 'type')
    list_display  = ('name', 'enabled', 'type_link')
    list_filter   = ('enabled', 'type')
    ordering      = ('type', 'name')
    search_fields = ('name', 'type__name')
admin.site.register(models.Derangement, DerangementAdmin)


class GenealogyAdmin (admin.ModelAdmin):
    list_display  = ('name', 'enabled')
    list_filter   = ('enabled',)
    ordering      = ('name',)
    search_fields = ('name',)
admin.site.register(models.Genealogy, GenealogyAdmin)


class MeritAdmin (admin.ModelAdmin):
    type_link     = make_admin_link(models.MeritType, 'type')
    list_display  = ('name', 'enabled', 'type_link', 'allowed_ratings', 'requires_specification', 'requires_description')
    list_filter   = ('enabled', 'type', 'requires_specification', 'requires_description')
    ordering      = ('type', 'name')
    search_fields = ('name', 'type__name')
admin.site.register(models.Merit, MeritAdmin)


class MiscTraitAdmin (admin.ModelAdmin):
    list_display  = ('name', 'enabled', 'requires_description')
    list_filter   = ('enabled', 'requires_description')
    ordering      = ('name',)
    search_fields = ('name',)
admin.site.register(models.MiscTrait, MiscTraitAdmin)


class PowerAdmin (admin.ModelAdmin):
    list_display       = ('group', 'name', 'enabled', 'rating')
    list_display_links = ('name',)
    ordering           = ('group', 'rating', 'name')
    search_fields      = ('group', 'name')
admin.site.register(models.Power, PowerAdmin)


class SkillAdmin (admin.ModelAdmin):
    type_link     = make_admin_link(models.SkillType, 'type')
    list_display  = ('name', 'enabled', 'type_link')
    list_filter   = ('enabled', 'type')
    ordering      = ('type', 'name')
    search_fileds = ('name', 'type__name')
admin.site.register(models.Skill, SkillAdmin)


class SubgroupAdmin (admin.ModelAdmin):
    list_display  = ('name', 'enabled')
    list_filter   = ('enabled',)
    ordering      = ('name',)
    search_fields = ('name',)
admin.site.register(models.Subgroup, SubgroupAdmin)
