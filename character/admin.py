from django.contrib import admin

from character import models
from common.admin import make_admin_link
from traits import models as trait_models


class XPRecordInline                   (admin.TabularInline): model = models.XPRecord
class CharacterHasAttributeInline      (admin.TabularInline): model = models.CharacterHasAttribute
class CharacterHasCombatTraitInline    (admin.TabularInline): model = models.CharacterHasCombatTrait
class CharacterHasDerangementInline    (admin.TabularInline): model = models.CharacterHasDerangement
class CharacterHasFlawInline           (admin.TabularInline): model = models.CharacterHasFlaw
class CharacterHasMeritInline          (admin.TabularInline): model = models.CharacterHasMerit
class CharacterHasMiscTraitInline      (admin.TabularInline): model = models.CharacterHasMiscTrait
class CharacterHasPowerInline          (admin.TabularInline): model = models.CharacterHasPower
class CharacterHasSkillInline          (admin.TabularInline): model = models.CharacterHasSkill
class CharacterHasSkillSpecialtyInline (admin.TabularInline): model = models.CharacterHasSkillSpecialty
class CharacterHasTextInline           (admin.TabularInline): model = models.CharacterHasText


class CharacterAdmin (admin.ModelAdmin):
    list_display = (
        'name', 'enabled', 'status', 'creature_type',
        'genealogy', 'affiliation', 'subgroup',
        'virtue', 'vice',
        'date_created', 'date_submitted', 'date_approved', 'date_last_edited',
    )
    list_filter = (
        'enabled', 'status', 'creature_type',
        'genealogy', 'affiliation', 'subgroup',
        'virtue', 'vice',
        'date_created', 'date_submitted', 'date_approved', 'date_last_edited',
    )
    inlines = [
        CharacterHasTextInline,
        CharacterHasAttributeInline,
        CharacterHasSkillInline,
        CharacterHasSkillSpecialtyInline,
        CharacterHasPowerInline,
        CharacterHasMeritInline,
        CharacterHasFlawInline,
        CharacterHasDerangementInline,
        CharacterHasCombatTraitInline,
        CharacterHasMiscTraitInline,
        XPRecordInline,
    ]
admin.site.register(models.Character, CharacterAdmin)


class _CHTAdminBase (admin.ModelAdmin):
    def edit_link (self, obj):
        return 'edit'
    edit_link.short_description = ''

    character_link = make_admin_link(models.Character, 'character')

    list_display  = ('edit_link', 'character_link', 'trait_link')
    list_filter   = ('trait', 'character')
    search_fields = ('character__name', 'trait__name')


class CharacterHasAttributeAdmin (_CHTAdminBase):
    trait_link   = make_admin_link(trait_models.Attribute, 'trait')
    list_display = _CHTAdminBase.list_display + ('rating',)
admin.site.register(models.CharacterHasAttribute, CharacterHasAttributeAdmin)


class CharacterHasCombatTraitAdmin (_CHTAdminBase):
    trait_link   = make_admin_link(trait_models.CombatTrait, 'trait')
    list_display = _CHTAdminBase.list_display + ('rating',)
admin.site.register(models.CharacterHasCombatTrait, CharacterHasCombatTraitAdmin)


class CharacterHasDerangementAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.Derangement, 'trait')
    list_display  = _CHTAdminBase.list_display  + ('specification',)
    search_fields = _CHTAdminBase.search_fields + ('specification', 'description')
admin.site.register(models.CharacterHasDerangement, CharacterHasDerangementAdmin)


class CharacterHasFlawAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.Flaw, 'trait')
    list_display  = _CHTAdminBase.list_display  + ('specification',)
    search_fields = _CHTAdminBase.search_fields + ('specification', 'description')
admin.site.register(models.CharacterHasFlaw, CharacterHasFlawAdmin)


class CharacterHasMeritAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.Merit, 'trait')
    list_display  = _CHTAdminBase.list_display  + ('specification', 'rating')
    search_fields = _CHTAdminBase.search_fields + ('specification', 'description')
admin.site.register(models.CharacterHasMerit, CharacterHasMeritAdmin)


class CharacterHasMiscTraitAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.MiscTrait, 'trait')
    list_display  = _CHTAdminBase.list_display  + ('rating',)
    search_fields = _CHTAdminBase.search_fields + ('description',)
admin.site.register(models.CharacterHasMiscTrait, CharacterHasMiscTraitAdmin)


class CharacterHasPowerAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.Power, 'trait')
    list_filter   = ('trait__group',) + _CHTAdminBase.list_filter
    search_fields = _CHTAdminBase.search_fields + ('trait__group',)
admin.site.register(models.CharacterHasPower, CharacterHasPowerAdmin)


class CharacterHasSkillAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.Skill, 'trait')
    list_display  = _CHTAdminBase.list_display  + ('rating',)
    search_fields = _CHTAdminBase.search_fields + ('character__name', 'trait__name')
admin.site.register(models.CharacterHasSkill, CharacterHasSkillAdmin)


class CharacterHasSkillSpecialtyAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.Skill, 'trait')
    list_display  = _CHTAdminBase.list_display  + ('specialty',)
    search_fields = _CHTAdminBase.search_fields + ('specialty',)
admin.site.register(models.CharacterHasSkillSpecialty, CharacterHasSkillSpecialtyAdmin)


class CharacterHasTextAdmin (_CHTAdminBase):
    trait_link    = make_admin_link(trait_models.CharacterText, 'trait')
    search_fields = _CHTAdminBase.search_fields + ('text',)
admin.site.register(models.CharacterHasText, CharacterHasTextAdmin)
