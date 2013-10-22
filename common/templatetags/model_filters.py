from django import template

from rest_framework.renderers import JSONRenderer


register = template.Library()


@register.filter
def display_fields (model):
    return ', '.join([
        "'{}'".format(field.name)
        for field
        in model._meta.fields
        if not str(field.name) in ['id']
    ])
display_fields.is_safe = True


@register.filter
def filter_fields (model):
    return ', '.join([
        "'{}'".format(field.name)
        for field
        in model._meta.fields
        if not str(field.name) in ['id', 'name']
    ])
filter_fields.is_safe = True


@register.filter
def meta (model, name):
    """
    Accesses the meta attribute of <model> known as 'name'.
    """
    return getattr(model._meta, name)


@register.filter
def related_parent (field):
    """
    Accesses the parent model of the related field for ForeignKey fields.
    """
    return field.related.parent_model


@register.filter
def serialize_json (obj):
    if hasattr(obj, '__iter__'):
        if len(obj) > 0:
            return JSONRenderer().render(obj[0].Serializer(obj, many = True).data)
        else:
            return '[]'
    else:
        if obj:
            return JSONRenderer().render(obj.Serializer(obj).data)
        else:
            return '{}'
serialize_json.is_safe = True
