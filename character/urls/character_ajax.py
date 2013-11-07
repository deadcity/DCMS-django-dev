# DCMS auto-generated file
# Mon, 4 Nov 2013 08:03:55 -0600 | 74e78fa434f79af99ce969a1285f06bc

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework.routers import DefaultRouter

from character import views

router = DefaultRouter()




router.register('Character', views.CharacterViewSet)



router.register('CharacterHasAttribute', views.CharacterHasAttributeViewSet)



router.register('CharacterHasCombatTrait', views.CharacterHasCombatTraitViewSet)



router.register('CharacterHasDerangement', views.CharacterHasDerangementViewSet)



router.register('CharacterHasFlaw', views.CharacterHasFlawViewSet)



router.register('CharacterHasMerit', views.CharacterHasMeritViewSet)



router.register('CharacterHasMiscTrait', views.CharacterHasMiscTraitViewSet)



router.register('CharacterHasPower', views.CharacterHasPowerViewSet)



router.register('CharacterHasSkill', views.CharacterHasSkillViewSet)



router.register('CharacterHasSkillSpecialty', views.CharacterHasSkillSpecialtyViewSet)



router.register('CharacterHasText', views.CharacterHasTextViewSet)




