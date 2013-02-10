from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from common.generators import generate_list_url, generate_detail_url
import traits
import traits.views as trait_views


_urls = []
for Model in traits.models._enum_models + traits.models._trait_models:
    model_name  = Model._meta.object_name
    module_name = Model._meta.module_name
    _urls.append(generate_list_url(
        module_name,
        getattr(trait_views, model_name + 'List')
    ))
    _urls.append(generate_detail_url(
        module_name,
        getattr(trait_views, model_name + 'Detail')
    ))


urlpatterns = patterns('', *_urls)
urlpatterns = format_suffix_patterns(urlpatterns)
