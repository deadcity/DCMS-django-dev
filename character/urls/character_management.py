from django.conf.urls import patterns, url

from character.views import character_management as views


urlpatterns = patterns('character.views.character_management',
    url(r'^$', 'character_list', name = 'character_list'),
    url(r'^(?P<pk>\d+)/show/$', views.ShowCharacterView.as_view(), name = 'show_character'),
)
