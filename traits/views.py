from django.db.models.loading import get_model
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer

from common.generators import generate_api_list, generate_api_detail
import traits
import traits.serializers as trait_serializers


for Model in traits.models._enum_models + traits.models._trait_models:
    model_name  = Model._meta.object_name
    Serializer  = getattr(trait_serializers, model_name + 'Serializer')
    list_name   = model_name + 'List'
    detail_name = model_name + 'Detail'
    globals()[list_name]   = generate_api_list  (list_name,   Model, Serializer)
    globals()[detail_name] = generate_api_detail(detail_name, Model, Serializer)


def generate_enum (request, enum_name):
    Model = get_model('traits', enum_name)
    serializer = getattr(trait_serializers, enum_name + 'Serializer')(
        Model.objects.all(),
        many = True
    )
    return render(request, 'traits/trait_enum.js', {
        'enum_name'   : enum_name,
        'values_json' : JSONRenderer().render(serializer.data),
    }, content_type = 'text/javascript')


def generate_trait_model (request, trait_name):
    return render(request, 'traits/trait_model.js', {
        'model_name' : trait_name,
        'Model'      : get_model('traits', trait_name),
    }, content_type = 'text/javascript')
