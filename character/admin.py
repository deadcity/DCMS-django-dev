from django.contrib import admin

import character.models as models
from common.generators import CharacterTraitAdmin_Metaclass, CharacterTraitInline_Metaclass


class CharacterHasAttributeAdmin      : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasAttribute)
class CharacterHasCombatTraitAdmin    : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasCombatTrait)
class CharacterHasDerangementAdmin    : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasDerangement)
class CharacterHasFlawAdmin           : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasFlaw)
class CharacterHasMeritAdmin          : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasMerit)
class CharacterHasMiscTraitAdmin      : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasMiscTrait)
class CharacterHasPowerAdmin          : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasPower)
class CharacterHasSkillAdmin          : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasSkill)
class CharacterHasSkillSpecialtyAdmin : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasSkillSpecialty)
class CharacterHasTextAdmin           : __metaclass__ = CharacterTraitAdmin_Metaclass(models.CharacterHasText)

admin.site.register(models.CharacterHasAttribute,      CharacterHasAttribute)
admin.site.register(models.CharacterHasCombatTrait,    CharacterHasCombatTrait)
admin.site.register(models.CharacterHasDerangement,    CharacterHasDerangement)
admin.site.register(models.CharacterHasFlaw,           CharacterHasFlaw)
admin.site.register(models.CharacterHasMerit,          CharacterHasMerit)
admin.site.register(models.CharacterHasMiscTrait,      CharacterHasMiscTrait)
admin.site.register(models.CharacterHasPower,          CharacterHasPower)
admin.site.register(models.CharacterHasSkill,          CharacterHasSkill)
admin.site.register(models.CharacterHasSkillSpecialty, CharacterHasSkillSpecialty)
admin.site.register(models.CharacterHasText,           CharacterHasText)

class CharacterHasAttributeInline      : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasAttribute)
class CharacterHasCombatTraitInline    : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasCombatTrait)
class CharacterHasDerangementInline    : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasDerangement)
class CharacterHasFlawInline           : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasFlaw)
class CharacterHasMeritInline          : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasMerit)
class CharacterHasMiscTraitInline      : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasMiscTrait)
class CharacterHasPowerInline          : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasPower)
class CharacterHasSkillInline          : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasSkill)
class CharacterHasSkillSpecialtyInline : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasSkillSpecialty)
class CharacterHasTextInline           : __metaclass__ = CharacterTraitInline_Metaclass(models.CharacterHasText)


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
admin.site.register(models.Character, CharacterAdmin)
