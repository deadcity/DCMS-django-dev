from django.contrib import admin

import character


def _create_character_trait_admin(model, model_name):
    field_list = []
    for field_name in [
            f.get_attname() for f
            in model._meta.fields]:
        if field_name in ('id', 'text', 'description'):
            continue
        elif '_id' == field_name[-3:]:
            field_list.append(field_name[:-3])
        else:
            field_list.append(field_name)

    Admin = type(
        model_name + 'Admin',
        (admin.ModelAdmin,),
        dict(
            list_display = tuple(field_list),
            list_filter  = tuple(field_list),
        )
    )

    admin.site.register(model, Admin)
    return Admin


for model in character.models._character_trait_models:
    model_name = model._meta.object_name
    globals()[model_name + 'Admin'] = _create_character_trait_admin(model, model_name)


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'enabled', 'creature_type',
        'genealogy', 'affiliation', 'subgroup',
        'virtue', 'vice',
        'date_created', 'date_submitted', 'date_approved', 'date_last_edited',
    )
    list_filter = (
        'enabled', 'creature_type',
        'genealogy', 'affiliation', 'subgroup',
        'virtue', 'vice',
        'date_created', 'date_submitted', 'date_approved', 'date_last_edited',
    )
admin.site.register(character.models.Character, CharacterAdmin)
