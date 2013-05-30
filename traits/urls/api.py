from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from traits_ajax import router

urlpatterns = patterns('',
    url(r'^', include(router.urls))
)
