from rest_framework import serializers

import traits


def _create_serializer(model):
    Meta = type(
        'Meta',
        (object,),
        dict(model = model)
    )
    return type(
        model._meta.object_name + 'Serializer',
        (serializers.ModelSerializer,),
        dict(Meta = Meta)
    )

for model in traits.models._enum_models + traits.models._trait_models:
    globals()[model._meta.object_name + 'Serializer'] = _create_serializer(model)
