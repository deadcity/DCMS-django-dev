from django import template

from rest_framework.renderers import JSONRenderer


register = template.Library()


@register.filter
def serialize_json(objects, serializer):
    serializer.object = objects
    return JSONRenderer().render(serializer.data)
serialize_json.is_safe = True
