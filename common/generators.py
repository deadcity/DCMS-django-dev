from django.conf.urls import url
from django.contrib import admin
from django.db import models
from django.forms.widgets import MediaDefiningClass

from rest_framework import generics, serializers


# admin

def CharacterTraitAdmin_Metaclass(Model):
    field_list = []
    for field_name in [f.get_attname() for f in Model._meta.fields]:
        if field_name in ('id', 'text', 'description'):
            continue
        elif '_id' == field_name[-3:]:
            field_list.append(field_name[:-3])
        else:
            field_list.append(field_name)

    class CharacterTraitAdmin_Metaclass(MediaDefiningClass):
        def __new__(metaclass, name, bases, attrs):
            return super(CharacterTraitAdmin_Metaclass, metaclass).__new__(
                metaclass, name, (admin.ModelAdmin,),
                dict(
                    list_display = tuple(field_list),
                    list_filter  = tuple(field_list),
                    **attrs
                )
            )
    return CharacterTraitAdmin_Metaclass

def CharacterTraitInline_Metaclass(Model):
    class CharacterTraitInline_Metaclass(MediaDefiningClass):
        def __new__(metaclass, name, bases, attrs):
            return super(CharacterTraitInline_Metaclass, metaclass).__new__(
                metaclass, name, (admin.TabularInline,),
                dict(model = Model, **attrs)
            )
    return CharacterTraitInline_Metaclass

def EnumAdmin_Metaclass(Model):
    class EnumAdmin_Metaclass(MediaDefiningClass):
        def __new__(metaclass, name, bases, attrs):
            return super(EnumAdmin_Metaclass, metaclass).__new__(
                metaclass, name, (admin.ModelAdmin,),
                dict(list_display = ('name',), **attrs)
            )
    return EnumAdmin_Metaclass

def TraitAdmin_Metaclass(Model):
    field_list = []
    for field_name in [f.get_attname() for f in Model._meta.fields]:
        if field_name in ('id', 'trait_ptr_id', 'name'):
            pass
        elif '_id' == field_name[-3:]:
            field_list.append(field_name[:-3])
        else:
            field_list.append(field_name)

    class TraitAdmin_Metaclass(MediaDefiningClass):
        def __new__(metaclass, name, bases, attrs):
            return super(TraitAdmin_Metaclass, metaclass).__new__(
                metaclass, name, (admin.ModelAdmin,),
                dict(
                    list_display = tuple(['name'] + field_list),
                    list_filter  = tuple(field_list),
                    **attrs
                )
            )
    return TraitAdmin_Metaclass


# models

class Model_Metaclass(models.base.ModelBase):
    def __new__(metaclass, name, bases, attrs):
        fields = {}

        for base in bases:
            if hasattr(base, 'fields'):
                fields.update(getattr(base, 'fields'))

        for key, val in attrs.items():
            if isinstance(val, models.fields.Field):
                fields[key] = val

        return super(Model_Metaclass, metaclass).__new__(
            metaclass, name, bases, dict(fields = fields, **attrs)
        )


# serializers

def Serializer_Metaclass(Model):
    class Serializer_Metaclass(serializers.SerializerMetaclass):
        def __new__(metaclass, name, bases, attrs):
            return super(Serializer_Metaclass, metaclass).__new__(
                metaclass, name, (serializers.ModelSerializer,),
                dict(Meta = type(
                    'Meta',
                    (object,),
                    dict(model = Model)
                ), **attrs)
            )
    return Serializer_Metaclass


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

def APIDetail_Metaclass(Model, Serializer):
    class APIDetail_Metaclass(type):
        def __new__(metaclass, name, bases, attrs):
            return super(APIDetail_Metaclass, metaclass).__new__(
                metaclass, name, (generics.RetrieveUpdateDestroyAPIView,),
                dict(
                    model            = Model,
                    serializer_class = Serializer,
                    **attrs
                )
            )
    return APIDetail_Metaclass

def APIList_Metaclass(Model, Serializer):
    class APIList_Metaclass(type):
        def __new__(metaclass, name, bases, attrs):
            return super(APIList_Metaclass, metaclass).__new__(
                metaclass, name, (generics.ListCreateAPIView,),
                dict(
                    model            = Model,
                    serializer_class = Serializer,
                    **attrs
                )
            )
    return APIList_Metaclass
