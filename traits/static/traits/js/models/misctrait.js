// DCMS auto-generated file
// 2013-05-13 11:58:31.554397

/* * * * * * * * * * * * * * * * * * * * * * *
 * DO NOT MODIFY THE CONTENTS OF THIS FILE!  *
 * * * * * * * * * * * * * * * * * * * * * * */

// If you wish to alter it's contents modify either the source model, or the
// generating tool and then run `manage.py generate_classes` again.  (Don't
// forget to commit the newly generated files!)


(function () {

var Models = Tools.create_namespace('Traits.Models');

Models.MiscTrait = Backbone.Model.extend({
    defaults: {
        id: null,
        name: null,
        enabled: null,
        requires_description: null,
    },

    parse: function (raw) {
        return {
            id: parseInt(raw.id, 10),
            name: raw.name,
            enabled: raw.enabled,
            requires_description: raw.requires_description,
        }
    },

    toJSON: function () {
        var attr = _.clone(this.attributes);

        return attr;
    },

    toHumanJSON: function () {
        var attr = _.clone(this.attributes);

        return attr;
    },

    url: function () {
        return '/api/traits/MiscTrait/' + (this.id == null ? '' : this.id + '/');
    },
});

})();
