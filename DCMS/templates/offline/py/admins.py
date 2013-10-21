{% extends 'offline/py/base.py' %}

{% load model_filters %}


{% block content %}

from django.contrib import admin

from {{ app_name }}.models import ({% for model in models %}
    {{ model|meta:"object_name" }}
{% endfor %})


{% for model in models %}
class {{ model|meta:"object_name" }}Admin (admin.ModelAdmin):
    list_display = ({{ model|display_fields }})
    list_filter  = ({{ model|filter_fields }})
admin.site.register({{ model|meta:"object_name" }}, {{ mdoel|meta:"object_name" }}Admin)
{% endfor %}

{% endblock content %}
