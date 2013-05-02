from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import character  # .models import character_trait_models
import character.views as character_views
from common.generators import generate_list_url, generate_detail_url


_urls = [
    generate_list_url  ('character', character_views.CharacterList),
    generate_detail_url('character', character_views.CharacterDetail),
]
# for Model in character.models._character_trait_models:
for model_name in dir(character.models):
    if "CharacterHas" in model_name:
        Model = getattr(character.models, model_name)
        module_name = Model._meta.module_name
        _urls.append(generate_list_url(
            module_name,
            getattr(character_views, model_name + 'List')
        ))
        _urls.append(generate_detail_url(
            module_name,
            getattr(character_views, model_name + 'Detail')
        ))


urlpatterns = patterns('',
    url(r'jsmodel/(?P<character_trait_name>\w+).js$', character_views.generate_character_trait_model, name = 'js_character_trait_model'),
    *_urls
)
# urlpatterns = format_suffix_patterns(urlpatterns)
