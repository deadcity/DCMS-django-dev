## @pachage dsqla.templatetags.dsqla.py
#  Some filters to use in django templates to help with processing SQLA models.


from django import template

from dsqla.models import ToJSON


register = template.Library()


_create_instance_format = "ORM.{Model._app_label}.{Model.__name__}.findOrCreate({json}, {{ parse: true }});"

@register.filter()
def create_js_records (obj):
    # Object is undefined or an empty iterable.
    if not obj:
        return ''

    # Object is an instance of a json-able model.
    if isinstance(obj, ToJSON):
        obj = [obj]

    return '\n'.join(
        _create_instance_format.format(
            Model = type(model),
            json = model.to_json()
        ) for model in obj
        if isinstance(model, ToJSON)
    )


@register.filter()
def serialize_json (obj):
    # Object is undefined.
    if obj is None:
        return '{}'

    # Object is an instance of a json-serializable model.
    if isinstance(obj, ToJSON):
        return obj.to_json()

    # Assume object is some kind of iterable.
    l = list(obj)
    if len(l) == 0:
        return '[]'
    return '[{}]'.format(', '.join(model.to_json() for model in l))
