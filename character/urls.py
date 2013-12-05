from common import routers
from character import views


# class Router(routers.DetailRouteMixin,
#              routers.ListRouteMixin,
#              routers.BaseRouter):
#     pass


router = routers.FullRouter()

router.register('',                           views.CharacterManagementViewSet, base_name = 'charactermanagement')
router.register('Character',                  views.CharacterViewSet)
router.register('CharacterHasAttribute',      views.CharacterHasAttributeViewSet)
router.register('CharacterHasCombatTrait',    views.CharacterHasCombatTraitViewSet)
router.register('CharacterHasDerangement',    views.CharacterHasDerangementViewSet)
router.register('CharacterHasFlaw',           views.CharacterHasFlawViewSet)
router.register('CharacterHasMerit',          views.CharacterHasMeritViewSet)
router.register('CharacterHasMiscTrait',      views.CharacterHasMiscTraitViewSet)
router.register('CharacterHasPower',          views.CharacterHasPowerViewSet)
router.register('CharacterHasSkill',          views.CharacterHasSkillViewSet)
router.register('CharacterHasSkillSpecialty', views.CharacterHasSkillSpecialtyViewSet)
router.register('CharacterHasText',           views.CharacterHasTextViewSet)
router.register('XPRecord',                   views.XPRecordViewSet)

urlpatterns = router.urls
