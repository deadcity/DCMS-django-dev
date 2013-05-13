from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from traits_ajax import urls

urlpatterns = patterns('', *urls)
# urlpatterns = format_suffix_patterns(urlpatterns)
