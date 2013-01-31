from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from traits.views import (
    AttributeTypeList, AttributeTypeDetail,
    AttributeList,     AttributeDetail,
    SkillTypeList,     SkillTypeDetail,
    SkillList,         SkillDetail
)


urlpatterns = patterns('',
    url(r'^api/attribute_type/$',                AttributeTypeList.as_view()),
    url(r'^api/attribute_type/(?P<pk>[0-9]+)/$', AttributeTypeDetail.as_view()),
    url(r'^api/attribute/$',                AttributeList.as_view()),
    url(r'^api/attribute/(?P<pk>[0-9]+)/$', AttributeDetail.as_view()),

    url(r'^api/skill_type/$',               SkillTypeList.as_view()),
    url(r'^api/skill_type(?P<pk>[0-9]+)/$', SkillTypeDetail.as_view()),
    url(r'^api/skill/$',               SkillList.as_view()),
    url(r'^api/skill(?P<pk>[0-9]+)/$', SkillDetail.as_view()),
)


urlpatterns = format_suffix_patterns(urlpatterns)
