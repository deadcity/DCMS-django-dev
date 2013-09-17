from django.conf.urls import include, patterns, url

from character_ajax import router


urlpatterns = patterns('',
    url(r'^', include(router.urls))
)
