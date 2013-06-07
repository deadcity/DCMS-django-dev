from django import template

from rest_framework.renderers import JSONRenderer


register = template.Library()


@register.filter
def serialize_json(obj):
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
