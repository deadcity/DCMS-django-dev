import re

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import traits.views as trait_views


def convert(s):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()

def create_url_list(model_name):
    return url(
        r'^api/' + convert(model_name) + '/$',
        getattr(trait_views, model_name + 'List').as_view()
    )

def create_url_detail(model_name):
    return url(
        r'^api/' + convert(model_name) + r'/(?P<pk>[0-9]+)/$',
        getattr(trait_views, model_name + 'Detail').as_view()
    )


urlpatterns = patterns('',
    create_url_list('AttributeType'),   create_url_detail('AttributeType'),
    create_url_list('DerangementType'), create_url_detail('DerangementType'),
    create_url_list('FlawType'),        create_url_detail('FlawType'),
    create_url_list('SkillType'),       create_url_detail('SkillType'),

    create_url_list('Attribute'),   create_url_detail('Attribute'),
    create_url_list('CombatTrait'), create_url_detail('CombatTrait'),
    create_url_list('Derangement'), create_url_detail('Derangement'),
    create_url_list('Flaw'),        create_url_detail('Flaw'),
    create_url_list('Skill'),       create_url_detail('Skill')
)


urlpatterns = format_suffix_patterns(urlpatterns)
