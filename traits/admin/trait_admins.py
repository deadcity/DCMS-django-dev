# DCMS auto-generated file
# 2013-09-23 10:18:14.789000

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.contrib import admin

from traits.models import Affiliation, Attribute, CharacterText, CombatTrait, CreatureType, Derangement, Flaw, Genealogy, Merit, MiscTrait, Power, Skill, Subgroup


class AffiliationAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(Affiliation, AffiliationAdmin)

class AttributeAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Attribute, AttributeAdmin)

class CharacterTextAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'hide_from_player',)
    list_filter  = ('enabled', 'hide_from_player',)
admin.site.register(CharacterText, CharacterTextAdmin)

class CombatTraitAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(CombatTrait, CombatTraitAdmin)

class CreatureTypeAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'genealogy_name', 'affiliation_name', 'subgroup_name', 'power_name',)
    list_filter  = ('enabled', 'genealogy_name', 'affiliation_name', 'subgroup_name', 'power_name',)
admin.site.register(CreatureType, CreatureTypeAdmin)

class DerangementAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type', 'requires_specification',)
    list_filter  = ('enabled', 'type', 'requires_specification',)
admin.site.register(Derangement, DerangementAdmin)

class FlawAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type', 'requires_specification', 'requires_description',)
    list_filter  = ('enabled', 'type', 'requires_specification', 'requires_description',)
admin.site.register(Flaw, FlawAdmin)

class GenealogyAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(Genealogy, GenealogyAdmin)

class MeritAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type', 'allowed_ratings', 'requires_specification', 'requires_description',)
    list_filter  = ('enabled', 'type', 'allowed_ratings', 'requires_specification', 'requires_description',)
admin.site.register(Merit, MeritAdmin)

class MiscTraitAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'requires_description',)
    list_filter  = ('enabled', 'requires_description',)
admin.site.register(MiscTrait, MiscTraitAdmin)

class PowerAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'rating', 'group',)
    list_filter  = ('enabled', 'rating', 'group',)
admin.site.register(Power, PowerAdmin)

class SkillAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(Skill, SkillAdmin)

class SubgroupAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(Subgroup, SubgroupAdmin)
