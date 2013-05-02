
(function () {

var Enum = Tools.create_namespace('Enum');

Enum.Element = Backbone.Model.extend({
    defaults: {
        id:   null,
        name: null,
        text: undefined,
    },

    name: function () {
        return this.get('name');
    },

    text: function () {
        var text = this.get('text');
        return text === undefined ? this.get('name') : text;
    },

    valueOf: function () {
        return this.id;
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
            // auto increment id
            var curr_val = el.id;
            if (_.isNull(curr_val) || _.isUndefined(curr_val)) {
                el.set('id', next_val);
                ++next_val;
            } else {
                next_val = curr_val + 1;
            }

            // Make enum elements 1st class members of the collection object.
            this_[el.get('name')] = el;
        });
    },

    get: function (identifier) {
        var element = Backbone.Collection.prototype.get.apply(this, arguments);
        if (element) return element;

        return this.find(function (item) {
            return item.get('name') == identifier;
        });
    },
})

})();
