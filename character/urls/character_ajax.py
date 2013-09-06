# DCMS auto-generated file
# 2013-05-30 12:10:52.781713

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework.routers import DefaultRouter

from character.views import CharacterViewSet, CharacterHasAttributeViewSet, CharacterHasCombatTraitViewSet, CharacterHasDerangementViewSet, CharacterHasFlawViewSet, CharacterHasMeritViewSet, CharacterHasMiscTraitViewSet, CharacterHasPowerViewSet, CharacterHasSkillViewSet, CharacterHasSkillSpecialtyViewSet, CharacterHasTextViewSet

router = DefaultRouter()
router.register('Character', CharacterViewSet)
router.register('CharacterHasAttribute', CharacterHasAttributeViewSet)
router.register('CharacterHasCombatTrait', CharacterHasCombatTraitViewSet)
router.register('CharacterHasDerangement', CharacterHasDerangementViewSet)
router.register('CharacterHasFlaw', CharacterHasFlawViewSet)
router.register('CharacterHasMerit', CharacterHasMeritViewSet)
router.register('CharacterHasMiscTrait', CharacterHasMiscTraitViewSet)
router.register('CharacterHasPower', CharacterHasPowerViewSet)
router.register('CharacterHasSkill', CharacterHasSkillViewSet)
router.register('CharacterHasSkillSpecialty', CharacterHasSkillSpecialtyViewSet)
router.register('CharacterHasText', CharacterHasTextViewSet)
