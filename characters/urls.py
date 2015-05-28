## @package characters.urls
#  URLs for character views.


from django.conf.urls import url

from characters import views


urlpatterns = [
    url(r'^$',                    views.character_list,    name = 'character-list'),
    url(r'^(?P<id>\d*)/submit$',  views.submit_character,  name = 'character-submit'),
    url(r'^(?P<id>\d*)/disable$', views.disable_character, name = 'character-disable'),
    url(r'^(?P<id>\d*)/enable$',  views.enable_character,  name = 'character-enable'),
]