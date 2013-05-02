from django import template
from django.db import models


register = template.Library()


@register.filter
def type_name(obj):
    return type(obj).__name__
type_name.is_safe = True


@register.filter
def field_type(Model, field_name):
    return type(Model.fields[field_name]).__name__
field_type.is_safe = True


@register.filter
def instance_name(Model):
    return Model._meta.verbose_name.replace(' ', '_')
instance_name.is_safe = True


@register.filter
def model_name(Model):
    return Model._meta.object_name
model_name.is_safe = True


# @register.filter
# def related_instance(Model, field_name):
#     return Modle._meta.fields[field_name].related.parent_model._meta.object_name
# related_instance.is_safe = True


@register.filter
def related_model(foreign_key):
    return foreign_key.related.parent_model


@register.filter
def module_name(obj):
    return obj.__module__


@register.filter
def split(s, delim = None):
    result = s.split(delim)
    # if target:
    #     return result[int(target)]
    return result
