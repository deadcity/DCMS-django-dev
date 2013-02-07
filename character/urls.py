import re

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import character


def _convert(s):
    s = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()

def _create_url_list(model_name):
    return url(
        r'^api/' + _convert(model_name) + '/$',
        getattr(character.views, model_name + 'List').as_view()
    )

def _create_url_detail(model_name):
    return url(
        r'^api/' + _convert(model_name) + r'/(?P<pk>[0-9]+)/$',
        getattr(character.views, model_name + 'Detail').as_view()
    )

_urls = [
    _create_url_list('Character'),
    _create_url_detail('Character'),
]
for model in character.models._character_trait_models:
    model_name = model._meta.object_name
    _urls.append(_create_url_list(model_name))
    _urls.append(_create_url_detail(model_name))


urlpatterns = patterns('', *_urls)
urlpatterns = format_suffix_patterns(urlpatterns)
