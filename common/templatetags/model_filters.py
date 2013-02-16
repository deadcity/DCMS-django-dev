from django import template
from django.db import models


register = template.Library()


@register.filter
def field_type(Model, field_name):
    return next(type(f).__name__
                for f in Model._meta.fields
                if f.name == field_name)
field_type.is_safe = True


@register.filter
def enum_name(Model, field_name):
    return next(f.related.parent_model._meta.object_name
                for f in Model._meta.fields
                if f.name == field_name)
enum_name.is_safe = True
