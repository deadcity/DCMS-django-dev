from common.generators import generate_serializer

import traits


for model in traits.models._enum_models + traits.models._trait_models:
    globals()[model._meta.object_name + 'Serializer'] = generate_serializer(model)
