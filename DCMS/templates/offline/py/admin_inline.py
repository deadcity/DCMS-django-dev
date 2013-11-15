{% extends 'offline/py/base.py' %}

{% load formatting_tags %}
{% load model_filters %}


{% block content %}

from django.contrib import admin

from {{ app_name }} import models


{% trimlines 3 %}
{% for model in models %}
{% with object_name=model|meta:'object_name' %}
class {{ object_name }}Inline (admin.TabularInline):
    model = models.{{ object_name }}
{% endwith %}
{% endfor %}
{% endtrimlines %}

{% endblock content %}
