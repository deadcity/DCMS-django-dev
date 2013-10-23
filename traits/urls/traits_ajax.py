# DCMS auto-generated file
# Wed, 23 Oct 2013 07:50:23 -0500 | 35d11303c9c11f30dd8aa8c22d76c61c

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework.routers import DefaultRouter

from traits import views

router = DefaultRouter()




router.register('AttributeType', views.AttributeType)



router.register('DerangementType', views.DerangementType)



router.register('FlawType', views.FlawType)



router.register('MeritType', views.MeritType)



router.register('SkillType', views.SkillType)



router.register('Status', views.Status)



router.register('Vice', views.Vice)



router.register('Virtue', views.Virtue)



router.register('Affiliation', views.Affiliation)



router.register('Attribute', views.Attribute)



router.register('CharacterText', views.CharacterText)



router.register('CombatTrait', views.CombatTrait)



router.register('CreatureType', views.CreatureType)



router.register('Derangement', views.Derangement)



router.register('Flaw', views.Flaw)



router.register('Genealogy', views.Genealogy)



router.register('Merit', views.Merit)



router.register('MiscTrait', views.MiscTrait)



router.register('Power', views.Power)



router.register('Skill', views.Skill)



router.register('Subgroup', views.Subgroup)




