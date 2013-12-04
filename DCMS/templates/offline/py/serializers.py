{% extends 'offline/py/base.py' %}

{% load formatting_tags %}
{% load model_filters %}


{% block content %}

from rest_framework import serializers

from {{ app_name }} import models


{% trimlines 3 %}
{% for model in models %}
{% with object_name=model|meta:'object_name' %}
class {{ object_name }}Serializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.{{ object_name }}
models.{{ object_name }}.Serializer = {{ object_name }}Serializer
{% endwith %}
{% endfor %}
{% endtrimlines %}

{% endblock content %}
