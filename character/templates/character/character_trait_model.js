{% load model_filters %}

(function () {

var Character = Tools.create_namespace('Character');

Character.{{model_name}} = Backbone.Model.extend({
    defaults: {
        id: null,
      {% for field in Model.fields %}
        {{field}}: null,
      {% endfor %}
    },

    parse: function (raw) {
        return {
            id: parseInt(raw.id, 10),
          {% for field in Model.fields %}
          {% if Model|field_type:field == 'IntegerField' %}
            {{field}}: parseInt(raw.{{field}}, 10),
          {% elif Model|field_type:field == 'SmallIntegerField' %}
            {{field}}: parseInt(raw.{{field}}, 10),
          {% elif Model|field_type:field == 'CharField' %}
            {{field}}: raw.{{field}},
          {% elif Model|field_type:field == 'TextField' %}
            {{field}}: raw.{{field}},
          {% elif Model|field_type:field == 'ForeignKey' %}
            {{field}}: Traits.{{Model|related_name:field}}.get(parseInt(raw.{{field}}, 10)),
          {% endif %}
          {% endfor %}
        }
    },

    toJSON: function () {
        var attr = _.clone(this.attributes);
      {% for field in Model.fields %}
      {% if Model|field_type:field == 'ForeignField' %}
        attr.{{field}} = attr.{{field}}.value();
      {% endif %}
      {% endfor %}
    },

    toHumanJSON: function () {
        var attr = _.clone(this.attributes);
      {% for field in Model.fields %}
      {% if Model|field_type:field == 'ForeignField' %}
        attr.{{field}} = attr.{{field}}.toHumanJSON();
      {% endif %}
      {% endfor %}
    },
});

})();
