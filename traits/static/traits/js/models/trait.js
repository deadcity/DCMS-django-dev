
(function () {

var Traits = Tools.create_namespace('Traits.Models');

Traits.Traits = Backbone.Model.extend({
    defaults: {
        id      : null,
        enabled : null,
        name    : null,
    },

    parse: function (raw) {
        return {
            id      : parseInt(raw.id),
            enabled : raw.enabled,
            name    : raw.name,
        }
    },

    toJSON: function () {
        return _.clone(this.attributes);
    },

    toHumanJSON: function () {
        return this.toJSON();
    },
})

})();
