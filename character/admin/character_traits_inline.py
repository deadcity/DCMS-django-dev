# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.contrib import admin

from character.models import CharacterHasAttribute, CharacterHasCombatTrait, CharacterHasDerangement, CharacterHasFlaw, CharacterHasMerit, CharacterHasMiscTrait, CharacterHasPower, CharacterHasSkill, CharacterHasSkillSpecialty, CharacterHasText


class CharacterHasAttributeInline (admin.TabularInline):
    model = CharacterHasAttribute

class CharacterHasCombatTraitInline (admin.TabularInline):
    model = CharacterHasCombatTrait

class CharacterHasDerangementInline (admin.TabularInline):
    model = CharacterHasDerangement

class CharacterHasFlawInline (admin.TabularInline):
    model = CharacterHasFlaw

class CharacterHasMeritInline (admin.TabularInline):
    model = CharacterHasMerit

class CharacterHasMiscTraitInline (admin.TabularInline):
    model = CharacterHasMiscTrait

class CharacterHasPowerInline (admin.TabularInline):
    model = CharacterHasPower

class CharacterHasSkillInline (admin.TabularInline):
    model = CharacterHasSkill

class CharacterHasSkillSpecialtyInline (admin.TabularInline):
    model = CharacterHasSkillSpecialty

class CharacterHasTextInline (admin.TabularInline):
    model = CharacterHasText
