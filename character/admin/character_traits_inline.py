# DCMS auto-generated file
# Mon, 4 Nov 2013 08:01:21 -0600 | 2b2f62b6de7ae83fc58a19af1d0b1f9f

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from django.contrib import admin

from character import models




class CharacterHasAttributeInline (admin.TabularInline):
    model = model.CharacterHasAttribute



class CharacterHasCombatTraitInline (admin.TabularInline):
    model = model.CharacterHasCombatTrait



class CharacterHasDerangementInline (admin.TabularInline):
    model = model.CharacterHasDerangement



class CharacterHasFlawInline (admin.TabularInline):
    model = model.CharacterHasFlaw



class CharacterHasMeritInline (admin.TabularInline):
    model = model.CharacterHasMerit



class CharacterHasMiscTraitInline (admin.TabularInline):
    model = model.CharacterHasMiscTrait



class CharacterHasPowerInline (admin.TabularInline):
    model = model.CharacterHasPower



class CharacterHasSkillInline (admin.TabularInline):
    model = model.CharacterHasSkill



class CharacterHasSkillSpecialtyInline (admin.TabularInline):
    model = model.CharacterHasSkillSpecialty



class CharacterHasTextInline (admin.TabularInline):
    model = model.CharacterHasText




