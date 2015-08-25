## @package characters.urls
#  URLs for character views.


from django.conf.urls import url

from characters import views


urlpatterns = [
    url(r'^$',                    views.character_list,    name = 'character-list'),
    url(r'^(?P<id>\d+)/edit$',    views.edit_character,    name = 'character-edit'),
    url(r'^(?P<id>\d+)/submit$',  views.submit_character,  name = 'character-submit'),
    url(r'^(?P<id>\d+)/disable$', views.disable_character, name = 'character-disable'),
    url(r'^(?P<id>\d+)/enable$',  views.enable_character,  name = 'character-enable'),

    url(r'^(?P<id>\d+)/available_traits$', views.available_traits,         name = 'character-available-traits'),
    url(r'^(?P<id>\d+)/update_summary$',   views.update_character_summary, name = 'character-update-summary'),

    url(r'^(?P<id>\d+)/character_trait/(?P<trait_id>\d*)$', views.CharacterTraitView.as_view(), name = 'character-update-trait'),
]
