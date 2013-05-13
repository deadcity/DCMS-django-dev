# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.conf.urls import url

from character.views import CharacterHasAttributeDetail, CharacterHasCombatTraitDetail, CharacterHasDerangementDetail, CharacterHasFlawDetail, CharacterHasMeritDetail, CharacterHasMiscTraitDetail, CharacterHasPowerDetail, CharacterHasSkillDetail, CharacterHasSkillSpecialtyDetail, CharacterHasTextDetail
from character.views import CharacterHasAttributeList, CharacterHasCombatTraitList, CharacterHasDerangementList, CharacterHasFlawList, CharacterHasMeritList, CharacterHasMiscTraitList, CharacterHasPowerList, CharacterHasSkillList, CharacterHasSkillSpecialtyList, CharacterHasTextList

urls = [
  url(r'^CharacterHasAttribute/(?P<pk>[0-9]+)/$', CharacterHasAttributeDetail.as_view()),
  url(r'^CharacterHasAttribute/$',                CharacterHasAttributeList.as_view()),

  url(r'^CharacterHasCombatTrait/(?P<pk>[0-9]+)/$', CharacterHasCombatTraitDetail.as_view()),
  url(r'^CharacterHasCombatTrait/$',                CharacterHasCombatTraitList.as_view()),

  url(r'^CharacterHasDerangement/(?P<pk>[0-9]+)/$', CharacterHasDerangementDetail.as_view()),
  url(r'^CharacterHasDerangement/$',                CharacterHasDerangementList.as_view()),

  url(r'^CharacterHasFlaw/(?P<pk>[0-9]+)/$', CharacterHasFlawDetail.as_view()),
  url(r'^CharacterHasFlaw/$',                CharacterHasFlawList.as_view()),

  url(r'^CharacterHasMerit/(?P<pk>[0-9]+)/$', CharacterHasMeritDetail.as_view()),
  url(r'^CharacterHasMerit/$',                CharacterHasMeritList.as_view()),

  url(r'^CharacterHasMiscTrait/(?P<pk>[0-9]+)/$', CharacterHasMiscTraitDetail.as_view()),
  url(r'^CharacterHasMiscTrait/$',                CharacterHasMiscTraitList.as_view()),

  url(r'^CharacterHasPower/(?P<pk>[0-9]+)/$', CharacterHasPowerDetail.as_view()),
  url(r'^CharacterHasPower/$',                CharacterHasPowerList.as_view()),

  url(r'^CharacterHasSkill/(?P<pk>[0-9]+)/$', CharacterHasSkillDetail.as_view()),
  url(r'^CharacterHasSkill/$',                CharacterHasSkillList.as_view()),

  url(r'^CharacterHasSkillSpecialty/(?P<pk>[0-9]+)/$', CharacterHasSkillSpecialtyDetail.as_view()),
  url(r'^CharacterHasSkillSpecialty/$',                CharacterHasSkillSpecialtyList.as_view()),

  url(r'^CharacterHasText/(?P<pk>[0-9]+)/$', CharacterHasTextDetail.as_view()),
  url(r'^CharacterHasText/$',                CharacterHasTextList.as_view()),
]
