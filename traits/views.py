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
