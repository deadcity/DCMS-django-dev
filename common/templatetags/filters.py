from django import template
from django.db import models


register = template.Library()


@register.filter
def attr(obj, name):
    """
    Accesses the member of 'obj' known as 'name'.
    """
    return getattr(obj, name);


@register.filter
def int_or_string(val):
    """
    Wraps the value in single quotes if it is a string (escaping as needed).
    Otherwise, passes on the value as is.
    """
    try:
        return int(val)
    except ValueError:
        return "'" + val.replace("'", "\\'") + "'"
int_or_string.is_safe = True


# TODO(emery): This is wrong.  Delete it and remove all uses of it.
@register.filter
def inherits(obj, class_name):
    Parent = type(obj)
    while True:
        if Parent.__name__ == class_name:
            return True
        elif Parent.__name__ == 'type':
            return False
        Parent = type(Parent)


@register.filter
def checkinstance(obj, class_name):
    module_path = class_name.split('.')
    fromlist = str('.'.join(module_path[:-2]))
    module = __import__('.'.join(module_path[:-1]), fromlist = fromlist)
    class_name = module_path[-1]
    if not hasattr(module, class_name):
        return False
    class_obj = getattr(module, class_name)
    if not isinstance(class_obj, type):
        return False
    return isinstance(obj, class_obj)


@register.filter
def classname(obj, class_name = None):
    obj_class_name = type(obj).__name__
    if class_name:
        if class_name == obj_class_name:
            return True
        else:
            return False
    else:
        return classname
