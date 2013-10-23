{% extends 'offline/py/base.py' %}

{% load model_filters %}


{% block content %}

from rest_framework.routers import DefaultRouter

from {{ app_name }} import views

router = DefaultRouter()


{% for model in models %}
{% with object_name=model|meta:'object_name' %}
router.register('{{ object_name }}', views.{{ object_name }}ViewSet)
{% endwith %}
{% endfor %}

{% endblock content %}
