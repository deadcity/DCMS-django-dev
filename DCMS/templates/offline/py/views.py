{% extends 'offline/py/base.py' %}

{% load model_filters %}


{% block content %}

from rest_framework import viewsets

from {{ app_name }} import models, serializers


{% for model in models %}
{% with object_name=model|meta:'object_name' %}
class {{ object_name }}ViewSet (viewsets.ModelViewSet):
    model            = models.{{ object_name }}
    serializer_class = serializers.{{ object_name }}Serializer
{% endwith %}
{% endfor %}

{% endblock content %}
