# DCMS auto-generated file
# Thu, 5 Dec 2013 08:39:39 -0600 | 23710cd6ce5878c7af2a8f4e32512b13

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from django.contrib import admin

from character import models


class XPRecordAdmin (admin.ModelAdmin):
    list_display = ('game', 'character', 'amount', 'note',)
    list_filter  = ('game', 'character', 'amount', 'note',)
admin.site.register(models.XPRecord, XPRecordAdmin)


class CharacterHasAttributeAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating',)
    list_filter  = ('character', 'trait', 'rating',)
admin.site.register(models.CharacterHasAttribute, CharacterHasAttributeAdmin)


class CharacterHasCombatTraitAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating',)
    list_filter  = ('character', 'trait', 'rating',)
admin.site.register(models.CharacterHasCombatTrait, CharacterHasCombatTraitAdmin)


class CharacterHasDerangementAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'specification', 'description',)
    list_filter  = ('character', 'trait', 'specification', 'description',)
admin.site.register(models.CharacterHasDerangement, CharacterHasDerangementAdmin)


class CharacterHasFlawAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'specification', 'description',)
    list_filter  = ('character', 'trait', 'specification', 'description',)
admin.site.register(models.CharacterHasFlaw, CharacterHasFlawAdmin)


class CharacterHasMeritAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating', 'specification', 'description',)
    list_filter  = ('character', 'trait', 'rating', 'specification', 'description',)
admin.site.register(models.CharacterHasMerit, CharacterHasMeritAdmin)


class CharacterHasMiscTraitAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating', 'description',)
    list_filter  = ('character', 'trait', 'rating', 'description',)
admin.site.register(models.CharacterHasMiscTrait, CharacterHasMiscTraitAdmin)


class CharacterHasPowerAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait',)
    list_filter  = ('character', 'trait',)
admin.site.register(models.CharacterHasPower, CharacterHasPowerAdmin)


class CharacterHasSkillAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating',)
    list_filter  = ('character', 'trait', 'rating',)
admin.site.register(models.CharacterHasSkill, CharacterHasSkillAdmin)


class CharacterHasSkillSpecialtyAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'specialty',)
    list_filter  = ('character', 'trait', 'specialty',)
admin.site.register(models.CharacterHasSkillSpecialty, CharacterHasSkillSpecialtyAdmin)


class CharacterHasTextAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'text',)
    list_filter  = ('character', 'trait', 'text',)
admin.site.register(models.CharacterHasText, CharacterHasTextAdmin)


