from django.conf.urls import patterns, url

from character.views import character_management as views


urlpatterns = patterns('character.views.character_management',
    url(r'^$',                  'character_list',                    name = 'character_list'),
    url(r'^(?P<pk>\d+)/show/$', 'character_detail',                  name = 'character_detail'),
    url(r'^(?P<pk>\d+)/edit/$', 'character_edit',                    name = 'character_edit'),
    url(r'^print_all/$',        'print_all',                         name = 'print_all'),
    url(r'^new/$',              'new_character',                     name = 'new_character'),
    url(r'^(?P<pk>\d+)/submit/$', 'character_submit',				 name = 'submit'),
)
