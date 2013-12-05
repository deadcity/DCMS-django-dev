# DCMS auto-generated file
# Thu, 5 Dec 2013 08:39:39 -0600 | 72b053599bcf8d1e813731e1a075a56c

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from django.contrib import admin

from character import models


class XPRecordInline (admin.TabularInline):
    model = models.XPRecord


class CharacterHasAttributeInline (admin.TabularInline):
    model = models.CharacterHasAttribute


class CharacterHasCombatTraitInline (admin.TabularInline):
    model = models.CharacterHasCombatTrait


class CharacterHasDerangementInline (admin.TabularInline):
    model = models.CharacterHasDerangement


class CharacterHasFlawInline (admin.TabularInline):
    model = models.CharacterHasFlaw


class CharacterHasMeritInline (admin.TabularInline):
    model = models.CharacterHasMerit


class CharacterHasMiscTraitInline (admin.TabularInline):
    model = models.CharacterHasMiscTrait


class CharacterHasPowerInline (admin.TabularInline):
    model = models.CharacterHasPower


class CharacterHasSkillInline (admin.TabularInline):
    model = models.CharacterHasSkill


class CharacterHasSkillSpecialtyInline (admin.TabularInline):
    model = models.CharacterHasSkillSpecialty


class CharacterHasTextInline (admin.TabularInline):
    model = models.CharacterHasText


