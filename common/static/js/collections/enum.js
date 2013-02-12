
(function () {

var Enum = Tools.create_namespace('Enum');

Enum.Element = Backbone.Model.extend({
    defaults: {
        name:  null,
        value: null,
        text:  undefined,
    },

    idAttribute: 'value',

    name: function () {
        return this.get('name');
    },

    value: function () {
        return this.get('value');
    },

    text: function () {
        var text = this.get('text');
        return text === undefined ? this.get('name') : text;
    },

    valueOf: function () {
        return this.value();
    },
});

Enum.Enum = Backbone.Collection.extend({
    model: Enum.Element,

    constructor: function (models, options) {
        // Call parent constructor.
        this.__proto__.__proto__.constructor.apply(this, arguments)

        var this_ = this;
        var next_val = 0;
        this.each(function (el) {
            // auto increment value
            var curr_val = el.get('value');
            if (_.isNull(curr_val) || _.isUndefined(curr_val)) {
                el.set('value', next_val);
                ++next_val;
            } else {
                next_val = curr_val + 1;
            }

            // Make enum elements 1st class members of the collection object.
            this_[el.get('name')] = el;
        });
    },

    get: function (identifier) {
        var element = Backbone.Collection.prototype.get.apply(this, identifier);
        if (element) return element;

        return this.find(function (item) {
            return item.get('name') == identifier;
        });
    },
})

})();
