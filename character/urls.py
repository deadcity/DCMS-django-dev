from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import character  # .models import character_trait_models
import character.views as character_views
from common.generators import generate_list_url, generate_detail_url


_urls = [
    generate_list_url  ('Character', character_views.CharacterList),
    generate_detail_url('Character', character_views.CharacterDetail),
]
for Model in character.models._character_trait_models:
    model_name = Model._meta.object_name
    _urls.append(generate_list_url(
        model_name,
        getattr(character_views, model_name + 'List')
    ))
    _urls.append(generate_detail_url(
        model_name,
        getattr(character_views, model_name + 'Detail')
    ))


urlpatterns = patterns('', *_urls)
urlpatterns = format_suffix_patterns(urlpatterns)
