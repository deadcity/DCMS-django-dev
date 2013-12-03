from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
    # url(r'^character/', include('character.urls')),
    url(r'^chronicle/', include('chronicle.urls.api')),
    # url(r'^traits/',    include('traits.urls')),
)
