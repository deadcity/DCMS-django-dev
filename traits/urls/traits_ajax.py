# DCMS auto-generated file
# 2013-09-10 11:58:03.321986

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from rest_framework.routers import DefaultRouter

from traits.views import AttributeTypeViewSet, DerangementTypeViewSet, FlawTypeViewSet, MeritTypeViewSet, SkillTypeViewSet, StatusViewSet, ViceViewSet, VirtueViewSet, AffiliationViewSet, AttributeViewSet, CharacterTextViewSet, CombatTraitViewSet, CreatureTypeViewSet, DerangementViewSet, FlawViewSet, GenealogyViewSet, MeritViewSet, MiscTraitViewSet, PowerViewSet, SkillViewSet, SubgroupViewSet

router = DefaultRouter()
router.register('AttributeType', AttributeTypeViewSet)
router.register('DerangementType', DerangementTypeViewSet)
router.register('FlawType', FlawTypeViewSet)
router.register('MeritType', MeritTypeViewSet)
router.register('SkillType', SkillTypeViewSet)
router.register('Status', StatusViewSet)
router.register('Vice', ViceViewSet)
router.register('Virtue', VirtueViewSet)
router.register('Affiliation', AffiliationViewSet)
router.register('Attribute', AttributeViewSet)
router.register('CharacterText', CharacterTextViewSet)
router.register('CombatTrait', CombatTraitViewSet)
router.register('CreatureType', CreatureTypeViewSet)
router.register('Derangement', DerangementViewSet)
router.register('Flaw', FlawViewSet)
router.register('Genealogy', GenealogyViewSet)
router.register('Merit', MeritViewSet)
router.register('MiscTrait', MiscTraitViewSet)
router.register('Power', PowerViewSet)
router.register('Skill', SkillViewSet)
router.register('Subgroup', SubgroupViewSet)
