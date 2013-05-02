{% load model_filters %}

(function () {

var Models = Tools.create_namespace('Character.Models');

Models.{{model_name}} = Backbone.Model.extend({
    defaults: {
        id:        null,
      {% for field in Model.fields %}
        {{field}}: null,
      {% endfor %}
    },

    parse: function (raw) {
        return {
            id:        parseInt(raw.id, 10),
          {% for field_name, field in Model.fields.items %}
          {% if field_name == 'character' %}
            character: parseInt(raw.{{field_name}}, 10),
          {% elif field|type_name == 'IntegerField' %}
            {{field_name}}: parseInt(raw.{{field_name}}, 10),
          {% elif field|type_name == 'SmallIntegerField' %}
            {{field_name}}: parseInt(raw.{{field_name}}, 10),
          {% elif field|type_name == 'CharField' %}
            {{field_name}}: raw.{{field_name}},
          {% elif field|type_name == 'TextField' %}
            {{field_name}}: raw.{{field_name}},
          {% elif field|type_name == 'ForeignKey' or field|type_name == 'EnumField' %}
            {{field_name}}: {{field|related_model|module_name|split:'.'|first|capfirst}}.Objects.{{field|related_model|model_name}}.get(parseInt(raw.{{field_name}}, 10)),
          {% else %}
            {{field_name}}: raw.{{field_name}},
          {% endif %}
          {% endfor %}
        }
    },

    toJSON: function () {
        var attr = _.clone(this.attributes);
      {% for field_name, field in Model.fields.items %}
      {% if field_name == 'character' %}
      {% elif field|type_name == 'ForeignKey' or field|type_name == 'EnumField' %}
        attr.{{field_name}} = attr.{{field_name}}.id;
      {% endif %}
      {% endfor %}
        return attr;
    },

    toHumanJSON: function () {
        var attr = _.clone(this.attributes);
      {% for field_name, field in Model.fields.items %}
      {% if field_name == 'character' %}
      {% elif field|type_name == 'ForeignKey' or field|type_name == 'EnumField' %}
        attr.{{field_name}} = attr.{{field_name}}.toHumanJSON();
      {% endif %}
      {% endfor %}
        return attr;
    },

    url: function () {
        return '/api/{{Model|module_name|split:'.'|first}}/jsmodel/{{model_name|lower}}/' + this.id + '/';
    },
});

})();
