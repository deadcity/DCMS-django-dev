from django.contrib import admin

import traits


def create_enum_admin(model_name):
    Admin = type(
        model_name + 'Admin',
        (admin.ModelAdmin,),
        dict(
            list_display = ('name',)
        )
    )
    admin.site.register(getattr(traits.models, model_name), Admin)
    return Admin


def create_admin(model_name):
    field_list = []
    for field_name in [
            f.get_attname() for f
            in getattr(traits.models, model_name)._meta.fields]:
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

    admin.site.register(getattr(traits.models, model_name), Admin)
    return Admin


AttributeTypeAdmin   = create_enum_admin('AttributeType')
DerangementTypeAdmin = create_enum_admin('DerangementType')
FlawTypeAdmin        = create_enum_admin('FlawType')
SkillTypeAdmin       = create_enum_admin('SkillType')

AttributeAdmin   = create_admin('Attribute')
CombatTraitAdmin = create_admin('CombatTrait')
DerangementAdmin = create_admin('Derangement')
FlawAdmin        = create_admin('Flaw')
SkillAdmin       = create_admin('Skill')
