{% load model_filters %}

(function () {

var Models = Tools.create_namespace('Character.Models');

Models.{{model_name}} = Backbone.Model.extend({
    defaults: {
        id:        null,
        character: null,
      {% for field in Model.fields %}
        {{field}}: null,
      {% endfor %}
    },

    parse: function (raw) {
        return {
            id:        parseInt(raw.id, 10),
            character: parseInt(raw.character, 10),
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
            {{field}}: Traits.{{Model|related_instance:field}}.get(parseInt(raw.{{field}}, 10)),
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
        return attr;
    },

    toHumanJSON: function () {
        var attr = _.clone(this.attributes);
      {% for field in Model.fields %}
        {{Model|field_type:field}}
      {% if Model|related_name:field == 'Character' %}
      {% elif Model|field_type:field == 'ForeignField' %}
        attr.{{field}} = attr.{{field}}.toHumanJSON();
      {% endif %}
      {% endfor %}
        return attr;
    },

    url: function () {
        return '/api/character/jsmodel/{{model_name|lower}}/' + this.id + '/';
    },
});

})();
