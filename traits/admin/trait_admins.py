# DCMS auto-generated file
# Tue, 22 Oct 2013 19:33:20 -0500 | e1e90a83e2c39839e0d2e2075861e732

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from django.contrib import admin

from traits import models




class AffiliationAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(models.Affiliation, AffiliationAdmin)



class AttributeAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(models.Attribute, AttributeAdmin)



class CharacterTextAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'hide_from_player',)
    list_filter  = ('enabled', 'hide_from_player',)
admin.site.register(models.CharacterText, CharacterTextAdmin)



class CombatTraitAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(models.CombatTrait, CombatTraitAdmin)



class CreatureTypeAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'genealogy_name', 'affiliation_name', 'subgroup_name', 'power_name',)
    list_filter  = ('enabled', 'genealogy_name', 'affiliation_name', 'subgroup_name', 'power_name',)
admin.site.register(models.CreatureType, CreatureTypeAdmin)



class DerangementAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type', 'requires_specification',)
    list_filter  = ('enabled', 'type', 'requires_specification',)
admin.site.register(models.Derangement, DerangementAdmin)



class FlawAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type', 'requires_specification', 'requires_description',)
    list_filter  = ('enabled', 'type', 'requires_specification', 'requires_description',)
admin.site.register(models.Flaw, FlawAdmin)



class GenealogyAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(models.Genealogy, GenealogyAdmin)



class MeritAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type', 'allowed_ratings', 'requires_specification', 'requires_description',)
    list_filter  = ('enabled', 'type', 'allowed_ratings', 'requires_specification', 'requires_description',)
admin.site.register(models.Merit, MeritAdmin)



class MiscTraitAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'requires_description',)
    list_filter  = ('enabled', 'requires_description',)
admin.site.register(models.MiscTrait, MiscTraitAdmin)



class PowerAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'rating', 'group',)
    list_filter  = ('enabled', 'rating', 'group',)
admin.site.register(models.Power, PowerAdmin)



class SkillAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name', 'type',)
    list_filter  = ('enabled', 'type',)
admin.site.register(models.Skill, SkillAdmin)



class SubgroupAdmin (admin.ModelAdmin):
    list_display = ('enabled', 'name',)
    list_filter  = ('enabled',)
admin.site.register(models.Subgroup, SubgroupAdmin)




