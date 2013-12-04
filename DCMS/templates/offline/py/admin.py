{% extends 'offline/py/base.py' %}

{% load formatting_tags %}
{% load model_filters %}


{% block content %}

from django.contrib import admin

from {{ app_name }} import models


{% trimlines 3 %}
{% for model in models %}
{% with object_name=model|meta:'object_name' %}
class {{ object_name }}Admin (admin.ModelAdmin):
    list_display = ({{ model|display_fields|safe }})
    list_filter  = ({{ model|filter_fields|safe }})
admin.site.register(models.{{ object_name }}, {{ object_name }}Admin)
{% endwith %}
{% endfor %}
{% endtrimlines %}

{% endblock content %}
