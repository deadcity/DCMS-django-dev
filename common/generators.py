from django.conf.urls import url
from django.contrib import admin
from rest_framework import generics, serializers


# admin

def generate_character_trait_admin(Model, model_name):
    print model_name, 'Trait Admin'
    field_list = []
    for field_name in [
            f.get_attname() for f
            in Model._meta.fields]:
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

    admin.site.register(Model, Admin)
    return Admin

def generate_character_trait_inline(Model, model_name):
    Inline = type(
        model_name + 'Inline',
        (admin.TabularInline,),
        dict(model = Model),
    )
    return Inline

def generate_enum_admin(Model, model_name):
    Admin = type(
        model_name + 'Admin',
        (admin.ModelAdmin,),
        dict(
            list_display = ('name',)
        )
    )
    admin.site.register(Model, Admin)
    return Admin

def generate_trait_admin(Model, model_name):
    field_list = []
    for field_name in [
            f.get_attname() for f
            in Model._meta.fields]:
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

    admin.site.register(Model, Admin)
    return Admin


# serializers

def generate_serializer(Model):
    Meta = type(
        'Meta',
        (object,),
        dict(model = Model)
    )
    return type(
        Model._meta.object_name + 'Serializer',
        (serializers.ModelSerializer,),
        dict(Meta = Meta)
    )


# urls

def generate_list_url(model_name, ListView):
    return url(
        r'^' + model_name + '/$',
        ListView.as_view()
    )

def generate_detail_url(model_name, DetailView):
    return url(
        r'^' + model_name + r'/(?P<pk>[0-9]+)/$',
        DetailView.as_view()
    )


# views

def generate_api_list(name, Model, Serializer):
    return type(
        name,
        (generics.ListCreateAPIView,),
        dict(
            model            = Model,
            serailizer_class = Serializer,
        )
    )

def generate_api_detail(name, Model, Serializer):
    return type(
        name,
        (generics.RetrieveUpdateDestroyAPIView,),
        dict(
            model            = Model,
            serializer_class = Serializer,
        )
    )
