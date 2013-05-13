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

Models.Merit = Backbone.Model.extend({
    defaults: {
        id: null,
        name: null,
        enabled: null,
        max_rating: null,
        inc_rating: null,
        requires_specification: null,
        requires_description: null,
        type: null,
        min_rating: null,
    },

    parse: function (raw) {
        return {
            id: parseInt(raw.id, 10),
            name: raw.name,
            enabled: raw.enabled,
            max_rating: parseInt(raw.max_rating, 10),
            inc_rating: parseInt(raw.inc_rating, 10),
            requires_specification: raw.requires_specification,
            requires_description: raw.requires_description,
            type: Traits.MeritType.get(parseInt(raw.type, 10)),
            min_rating: parseInt(raw.min_rating, 10),
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
        return '/api/traits/Merit/' + (this.id == null ? '' : this.id + '/');
    },
});

})();
