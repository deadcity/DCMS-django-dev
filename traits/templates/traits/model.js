{% load model_filters %}

(function () {

var Traits = Tools.create_namespace('Traits');

Traits.{{model_name}} = Backbone.Model.extend({
    defaults: {
        id: null,
      {% for field in Model.fields %}
        {{field}}: null,
      {% endfor %}
    },

    parse: function (raw) {
        return {
            id: raw.id,
          {% for field in Model.fields %}
          {% if Model|field_type:field == 'IntegerField' %}
            {{field}}: parseInt(raw.{{field}}),
          {% elif Model|field_type:field == 'SmallIntegerField' %}
            {{field}}: parseInt(raw.{{field}}),
          {% elif Model|field_type:field == 'EnumField' %}
            {{field}}: Traits.{{Model|enum_name:field}}.get(parseInt(raw.{{field}})),
          {% else %}
            {{field}}: raw.{{field}},
          {% endif %}
          {% endfor %}
        }
    },

    toJSON: function () {
        var attr = _.clone(this.attributes);
      {% for field in Model.fields %}
      {% if Model|field_type:field == 'EnumField' %}
        attr.{{field}} = attr.{{field}}.value();
      {% endif %}
      {% endfor %}
    },

    toHumanJSON: function () {
        var attr = _.clone(this.attributes);
      {% for field in Model.fields %}
      {% if Model|field_type:field == 'EnumField' %}
        attr.{{field}} = attr.{{field}}.toHumanJSON();
      {% endif %}
      {% endfor %}
    },
});

})();
