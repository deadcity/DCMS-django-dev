from django.contrib import admin

import character
from common.generators import generate_character_trait_admin, generate_character_trait_inline


for Model in character.models._character_trait_models:
    model_name = Model._meta.object_name
    globals()[model_name + 'Admin']  = generate_character_trait_admin(Model, model_name)
    globals()[model_name + 'Inline'] = generate_character_trait_inline(Model, model_name)


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'enabled', 'creature_type',
        'genealogy', 'affiliation', 'subgroup',
        'virtue', 'vice',
        'date_created', 'date_submitted', 'date_approved', 'date_last_edited',
    )
    list_filter = (
        'enabled', 'creature_type',
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
admin.site.register(character.models.Character, CharacterAdmin)
