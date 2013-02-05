from django.contrib import admin

import traits


def _create_enum_admin(model, model_name):
    Admin = type(
        model_name + 'Admin',
        (admin.ModelAdmin,),
        dict(
            list_display = ('name',)
        )
    )
    admin.site.register(model, Admin)
    return Admin


def _create_trait_admin(model, model_name):
    field_list = []
    for field_name in [
            f.get_attname() for f
            in model._meta.fields]:
        if field_name in ('id', 'trait_ptr_id', 'name'):
            pass
        elif '_id' == field_name[-3:]:
            field_list.append(field_name[:-3])
        else:
            field_list.append(field_name)

    Admin = type(
        model_name + 'Admin',
        (admin.ModelAdmin,),
        dict(
            list_display = tuple(['name'] + field_list),
            list_filter  = tuple(field_list),
        )
    )

    admin.site.register(model, Admin)
    return Admin


for model in traits.models._enum_models:
    model_name = model._meta.object_name
    globals()[model_name + 'Admin'] = _create_enum_admin(model, model_name)

for model in traits.models._trait_models:
    model_name = model._meta.object_name
    globals()[model_name + 'Admin'] = _create_trait_admin(model, model_name)
