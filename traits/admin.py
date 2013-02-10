from common.generators import generate_enum_admin, generate_trait_admin
import traits


for Model in traits.models._enum_models:
    model_name = Model._meta.object_name
    globals()[model_name + 'Admin'] = generate_enum_admin(Model, model_name)

for Model in traits.models._trait_models:
    model_name = Model._meta.object_name
    globals()[model_name + 'Admin'] = generate_trait_admin(Model, model_name)
