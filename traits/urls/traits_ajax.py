# DCMS auto-generated file
# Fri, 15 Nov 2013 07:34:32 -0600 | 53acbaa14707f375c585738ddfdbf0d1

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework.routers import DefaultRouter

from traits import views


router = DefaultRouter()

router.register('AttributeType', views.AttributeTypeViewSet)
router.register('DerangementType', views.DerangementTypeViewSet)
router.register('FlawType', views.FlawTypeViewSet)
router.register('MeritType', views.MeritTypeViewSet)
router.register('SkillType', views.SkillTypeViewSet)
router.register('Vice', views.ViceViewSet)
router.register('Virtue', views.VirtueViewSet)
router.register('Affiliation', views.AffiliationViewSet)
router.register('Attribute', views.AttributeViewSet)
router.register('CharacterText', views.CharacterTextViewSet)
router.register('CombatTrait', views.CombatTraitViewSet)
router.register('CreatureType', views.CreatureTypeViewSet)
router.register('Derangement', views.DerangementViewSet)
router.register('Flaw', views.FlawViewSet)
router.register('Genealogy', views.GenealogyViewSet)
router.register('Merit', views.MeritViewSet)
router.register('MiscTrait', views.MiscTraitViewSet)
router.register('Power', views.PowerViewSet)
router.register('Skill', views.SkillViewSet)
router.register('Subgroup', views.SubgroupViewSet)


