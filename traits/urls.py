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

urlpatterns = router.urls
