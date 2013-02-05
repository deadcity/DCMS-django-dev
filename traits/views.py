from rest_framework import generics

import traits
import traits.serializers as trait_serializers


def _create_api_list(model, model_name):
    return type(
        model_name + 'List',
        (generics.ListCreateAPIView,),
        dict(
            model            = model,
            serializer_class = getattr(trait_serializers, model_name + 'Serializer')
        )
    )

def _create_api_detail(model, model_name):
    return type(
        model_name + 'Detail',
        (generics.RetrieveUpdateDestroyAPIView,),
        dict(
            model            = model,
            serializer_class = getattr(trait_serializers, model_name + 'Serializer')
        )
    )

for model in traits.models._enum_models + traits.models._trait_models:
    model_name = model._meta.object_name
    globals()[model_name + 'List']   = _create_api_list  (model, model_name)
    globals()[model_name + 'Detail'] = _create_api_detail(model, model_name)
