from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from character_ajax import urls as character_urls
from character_traits_ajax import urls as character_trait_urls


urlpatterns = patterns('', *(character_urls + character_trait_urls))
# urlpatterns = format_suffix_patterns(urlpatterns)
