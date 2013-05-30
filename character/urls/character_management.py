from django.conf.urls import patterns, url

urlpatterns = patterns('character.views.character_management',
    url(r'^$', 'character_list', name = 'character_list')
)
