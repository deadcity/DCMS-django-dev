{% extends 'offline/py/base.py' %}

{% load model_filters %}


{% block content %}

from rest_framework import serializers

from {{ app_name }} import models


{% for model in models %}
{% with object_name=model|meta:'object_name' %}
class {{ object_name }}Serializer (serializers.ModelSerializer):
    class Meta (object):
        model = models.{{ object_name }}
models.{{ object_name }}.Serializer = {{ object_name }}Serializer
{% endwith %}
{% endfor %}

{% endblock content %}
