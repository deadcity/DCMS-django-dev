from django.contrib import admin

from character_traits_inline import *

from character import models


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
    ]

admin.site.register(models.Character, CharacterAdmin)
