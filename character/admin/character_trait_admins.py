# DCMS auto-generated file
# 2013-09-10 11:58:03.321986

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.contrib import admin

from character.models import CharacterHasAttribute, CharacterHasCombatTrait, CharacterHasDerangement, CharacterHasFlaw, CharacterHasMerit, CharacterHasMiscTrait, CharacterHasPower, CharacterHasSkill, CharacterHasSkillSpecialty, CharacterHasText


class CharacterHasAttributeAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating',)
    list_filter  = ('character', 'trait', 'rating',)
admin.site.register(CharacterHasAttribute, CharacterHasAttributeAdmin)

class CharacterHasCombatTraitAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating',)
    list_filter  = ('character', 'trait', 'rating',)
admin.site.register(CharacterHasCombatTrait, CharacterHasCombatTraitAdmin)

class CharacterHasDerangementAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'specification', 'description',)
    list_filter  = ('character', 'trait', 'specification', 'description',)
admin.site.register(CharacterHasDerangement, CharacterHasDerangementAdmin)

class CharacterHasFlawAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'specification', 'description',)
    list_filter  = ('character', 'trait', 'specification', 'description',)
admin.site.register(CharacterHasFlaw, CharacterHasFlawAdmin)

class CharacterHasMeritAdmin (admin.ModelAdmin):
    list_display = ('character', 'rating', 'description', 'trait', 'specification',)
    list_filter  = ('character', 'rating', 'description', 'trait', 'specification',)
admin.site.register(CharacterHasMerit, CharacterHasMeritAdmin)

class CharacterHasMiscTraitAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'description', 'rating',)
    list_filter  = ('character', 'trait', 'description', 'rating',)
admin.site.register(CharacterHasMiscTrait, CharacterHasMiscTraitAdmin)

class CharacterHasPowerAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait',)
    list_filter  = ('character', 'trait',)
admin.site.register(CharacterHasPower, CharacterHasPowerAdmin)

class CharacterHasSkillAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'rating',)
    list_filter  = ('character', 'trait', 'rating',)
admin.site.register(CharacterHasSkill, CharacterHasSkillAdmin)

class CharacterHasSkillSpecialtyAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'specialty',)
    list_filter  = ('character', 'trait', 'specialty',)
admin.site.register(CharacterHasSkillSpecialty, CharacterHasSkillSpecialtyAdmin)

class CharacterHasTextAdmin (admin.ModelAdmin):
    list_display = ('character', 'trait', 'text',)
    list_filter  = ('character', 'trait', 'text',)
admin.site.register(CharacterHasText, CharacterHasTextAdmin)
