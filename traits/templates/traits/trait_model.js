{% load model_filters %}

(function () {

var Models = Tools.create_namespace('Traits.Models');

Models.{{model_name}} = Backbone.Model.extend({
    defaults: {
        id: null,
      {% for field in Model.fields %}
        {{field}}: null,
      {% endfor %}
    },

    initialize: function (attributes) {
        this.set(this.parse(attributes));
    },

    parse: function (raw) {
        return {
            id: parseInt(raw.id, 10),
          {% for field in Model.fields %}
          {% if Model|field_type:field == 'IntegerField' %}
            {{field}}: parseInt(raw.{{field}}, 10),
          {% elif Model|field_type:field == 'SmallIntegerField' %}
            {{field}}: parseInt(raw.{{field}}, 10),
          {% elif Model|field_type:field == 'EnumField' %}
            {{field}}: Traits.{{Model|related_name:field}}.get(parseInt(raw.{{field}}, 10)),
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

    url: function () {
        return '/api/traits/jsmodel/{{model_name|lower}}/' + this.id + '/';
    },
});

})();
