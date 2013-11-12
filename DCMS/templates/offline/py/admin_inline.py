{% extends 'offline/py/base.py' %}

{% load model_filters %}


{% block content %}

from django.contrib import admin

from {{ app_name }} import models


{% for model in models %}
{% with object_name=model|meta:'object_name' %}
class {{ object_name }}Inline (admin.TabularInline):
    model = models.{{ object_name }}
{% endwith %}
{% endfor %}

{% endblock content %}
