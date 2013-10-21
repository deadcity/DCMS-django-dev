{% extends 'offline/py/base.py' %}

{% load model_filters %}


{% block content %}

from django.contrib import admin

from {{ app_name }}.models import ({% for model in models %}
    {{ model:meta:"object_name" }}
{% endfor %})


{% for model in models %}
class {{ model|meta:"object_name" }}Inline (admin.TabularInline):
    model = {{ model|meta:"object_name" }}
{% endfor %}

{% endblock content %}
