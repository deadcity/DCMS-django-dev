from django import template


register = template.Library()


@register.filter
def get_range(value):
    return range(0 if value is None else value)
get_range.is_safe = True
