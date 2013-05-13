# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.conf.urls import url

from traits.views import AttributeTypeDetail, DerangementTypeDetail, FlawTypeDetail, MeritTypeDetail, SkillTypeDetail, ViceDetail, VirtueDetail, AffiliationDetail, AttributeDetail, CharacterTextDetail, CombatTraitDetail, CreatureTypeDetail, DerangementDetail, FlawDetail, GenealogyDetail, MeritDetail, MiscTraitDetail, PowerDetail, SkillDetail, SubgroupDetail
from traits.views import AttributeTypeList, DerangementTypeList, FlawTypeList, MeritTypeList, SkillTypeList, ViceList, VirtueList, AffiliationList, AttributeList, CharacterTextList, CombatTraitList, CreatureTypeList, DerangementList, FlawList, GenealogyList, MeritList, MiscTraitList, PowerList, SkillList, SubgroupList

urls = [
  url(r'^AttributeType/(?P<pk>[0-9]+)/$', AttributeTypeDetail.as_view()),
  url(r'^AttributeType/$',                AttributeTypeList.as_view()),

  url(r'^DerangementType/(?P<pk>[0-9]+)/$', DerangementTypeDetail.as_view()),
  url(r'^DerangementType/$',                DerangementTypeList.as_view()),

  url(r'^FlawType/(?P<pk>[0-9]+)/$', FlawTypeDetail.as_view()),
  url(r'^FlawType/$',                FlawTypeList.as_view()),

  url(r'^MeritType/(?P<pk>[0-9]+)/$', MeritTypeDetail.as_view()),
  url(r'^MeritType/$',                MeritTypeList.as_view()),

  url(r'^SkillType/(?P<pk>[0-9]+)/$', SkillTypeDetail.as_view()),
  url(r'^SkillType/$',                SkillTypeList.as_view()),

  url(r'^Vice/(?P<pk>[0-9]+)/$', ViceDetail.as_view()),
  url(r'^Vice/$',                ViceList.as_view()),

  url(r'^Virtue/(?P<pk>[0-9]+)/$', VirtueDetail.as_view()),
  url(r'^Virtue/$',                VirtueList.as_view()),

  url(r'^Affiliation/(?P<pk>[0-9]+)/$', AffiliationDetail.as_view()),
  url(r'^Affiliation/$',                AffiliationList.as_view()),

  url(r'^Attribute/(?P<pk>[0-9]+)/$', AttributeDetail.as_view()),
  url(r'^Attribute/$',                AttributeList.as_view()),

  url(r'^CharacterText/(?P<pk>[0-9]+)/$', CharacterTextDetail.as_view()),
  url(r'^CharacterText/$',                CharacterTextList.as_view()),

  url(r'^CombatTrait/(?P<pk>[0-9]+)/$', CombatTraitDetail.as_view()),
  url(r'^CombatTrait/$',                CombatTraitList.as_view()),

  url(r'^CreatureType/(?P<pk>[0-9]+)/$', CreatureTypeDetail.as_view()),
  url(r'^CreatureType/$',                CreatureTypeList.as_view()),

  url(r'^Derangement/(?P<pk>[0-9]+)/$', DerangementDetail.as_view()),
  url(r'^Derangement/$',                DerangementList.as_view()),

  url(r'^Flaw/(?P<pk>[0-9]+)/$', FlawDetail.as_view()),
  url(r'^Flaw/$',                FlawList.as_view()),

  url(r'^Genealogy/(?P<pk>[0-9]+)/$', GenealogyDetail.as_view()),
  url(r'^Genealogy/$',                GenealogyList.as_view()),

  url(r'^Merit/(?P<pk>[0-9]+)/$', MeritDetail.as_view()),
  url(r'^Merit/$',                MeritList.as_view()),

  url(r'^MiscTrait/(?P<pk>[0-9]+)/$', MiscTraitDetail.as_view()),
  url(r'^MiscTrait/$',                MiscTraitList.as_view()),

  url(r'^Power/(?P<pk>[0-9]+)/$', PowerDetail.as_view()),
  url(r'^Power/$',                PowerList.as_view()),

  url(r'^Skill/(?P<pk>[0-9]+)/$', SkillDetail.as_view()),
  url(r'^Skill/$',                SkillList.as_view()),

  url(r'^Subgroup/(?P<pk>[0-9]+)/$', SubgroupDetail.as_view()),
  url(r'^Subgroup/$',                SubgroupList.as_view()),
]
