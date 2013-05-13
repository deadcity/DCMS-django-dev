# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.contrib import admin

from traits.models import Affiliation, Attribute, CharacterText, CombatTrait, CreatureType, Derangement, Flaw, Genealogy, Merit, MiscTrait, Power, Skill, Subgroup


class AffiliationAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter  = ('enabled',)
admin.site.register(Affiliation, AffiliationAdmin)

class AttributeAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Attribute, AttributeAdmin)

class CharacterTextAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'hide_from_player',)
    list_filter  = ('enabled', 'hide_from_player',)
admin.site.register(CharacterText, CharacterTextAdmin)

class CombatTraitAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter  = ('enabled',)
admin.site.register(CombatTrait, CombatTraitAdmin)

class CreatureTypeAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'affiliation_name', 'genealogy_name', 'subgroup_name', 'power_name',)
    list_filter  = ('enabled', 'affiliation_name', 'genealogy_name', 'subgroup_name', 'power_name',)
admin.site.register(CreatureType, CreatureTypeAdmin)

class DerangementAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'requires_specification', 'type',)
    list_filter  = ('enabled', 'requires_specification', 'type',)
admin.site.register(Derangement, DerangementAdmin)

class FlawAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'requires_specification', 'requires_description', 'type',)
    list_filter  = ('enabled', 'requires_specification', 'requires_description', 'type',)
admin.site.register(Flaw, FlawAdmin)

class GenealogyAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter  = ('enabled',)
admin.site.register(Genealogy, GenealogyAdmin)

class MeritAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'max_rating', 'inc_rating', 'requires_specification', 'requires_description', 'type', 'min_rating',)
    list_filter  = ('enabled', 'max_rating', 'inc_rating', 'requires_specification', 'requires_description', 'type', 'min_rating',)
admin.site.register(Merit, MeritAdmin)

class MiscTraitAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'requires_description',)
    list_filter  = ('enabled', 'requires_description',)
admin.site.register(MiscTrait, MiscTraitAdmin)

class PowerAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'rating', 'group',)
    list_filter  = ('enabled', 'rating', 'group',)
admin.site.register(Power, PowerAdmin)

class SkillAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Skill, SkillAdmin)

class SubgroupAdmin (admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    list_filter  = ('enabled',)
admin.site.register(Subgroup, SubgroupAdmin)
