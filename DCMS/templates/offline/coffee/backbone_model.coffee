{% extends 'offline/coffee/base.coffee' %}

{% load filters %}
{% load model_filters %}


{% block content %}
Models = Tools.create_namespace '{{ model|meta:'app_label'|title }}.Models'

class Models.{{ model|meta:'object_name' }} extends Backbone.Model
    defaults:
      {% for field in model|meta:'fields' %}
        {{ field.name }}: null
      {% endfor %}

    parse: (raw) ->
      {% for field in model|meta:'fields' %}
      {% if field.name == 'character' %}
        {{ field.name }}: parseInt raw.character, 10
      {% elif field|checkinstance:'django.db.models.fields.AutoField' %}
        {{ field.name }}: parseInt raw.{{ field.name }}, 10
      {% elif field|checkinstance:'django.db.models.fields.IntegerField' %}
        {{ field.name }}: parseInt raw.{{ field.name }}, 10
      {% elif field|checkinstance:'django.db.models.fields.CommaSeparatedIntegerField' %}
        {{ field.name }}: parseInt i, 10 for i in raw.{{ field.name }}.split ','
      {% elif field|checkinstance:'django.db.models.fields.CharField' %}
        {{ field.name }}: raw.{{ field.name }}
      {% elif field|checkinstance:'django.db.models.fields.TextField' %}
        {{ field.name }}: raw.{{ field.name }}
      {% elif field|checkinstance:'traits.models.EnumModelKey' %}
        {{ field.name }}: {{ field|related_parent|meta:'app_label'|title }}.Enums.{{ field|related_parent|meta:'object_name' }}.get raw.{{ field.name }}
      {% elif field|checkinstance:'common.fields.EnumField' %}
        {# TODO(emery): finish defining #}
        {# {{ field.name }}: {{ model|meta:'app_label'|title }}.Enum.{{ field.enum. }} #}
      {% elif field|checkinstance:'django.db.models.fields.ForeignKey' %}
        {{ field.name }}: {{ field|related_parent|meta:'app_label'|title }}.Objects.{{ field|related_parent|meta:'object_name' }}.get raw.{{ field.name }}
      {% else %}
        {{ field.name }}: raw.{{ field.name }}
      {% endif %}
      {% endfor %}

    toJSON: () ->
        attr = _.clone @attributes
      {% for field in model|meta:'fields' %}
      {% if field|checkinstance:'django.db.models.CommaSeparatedIntegerField' %}
        attr.{{ field.name }} = attr.{{ field.name }}.join()
      {% elif field|checkinstance:'django.db.models.ForeignKey' %}
        attr.{{ field.name }} = attr.{{ field.name }}.id
      {% endif %}
      {% endfor %}
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      {% for field in model|meta:'fields' %}
      {% if field|checkinstance:'traits.models.EnumModelKey' %}
      {% elif field|checkinstance:'django.db.models.ForeignKey' %}
        attr.{{ field.name }} = attr.{{ field.name }}.toHumanJSON()
      {% endif %}
      {% endfor %}
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/{{ model|meta:'app_label' }}/{{ model|meta:'object_name' }}/#{ if @id? then "#{ @id }/" else '' }"
{% endblock content %}
