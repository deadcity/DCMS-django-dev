from django import template
from django.db import models


register = template.Library()


@register.filter
def js_bool(value):
    return 'true' if value else 'false'
js_bool.is_safe = True
