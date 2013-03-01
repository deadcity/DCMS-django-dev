
(function () {

var Models = Tools.create_namespace('Character.Models');

Models.Character = Backbone.Model.extend({
    defaults: {
        id      : null,
        enabled : false,
        user    : null,

        name          : null,
        creature_type : null,
        genealogy     : null,
        affiliation   : null,
        subgroup      : null,
        virtue        : null,
        vice          : null,

        date_created     : null,
        date_submitted   : null,
        date_approved    : null,
        date_last_edited : null,
    },

    parse: function (raw) {
        return {
            id      : parseInt(raw.id, 10),
            enabled : raw.enabled,
            user    : parseInt(raw.id, 10),

            name          : raw.name,
            creature_type : Traits.creature_type .get(raw.creature_type),
            genealogy     : Traits.genealogy     .get(raw.genealogy),
            affiliation   : Traits.affiliation   .get(raw.affiliation),
            subgroup      : Traits.subgroup      .get(raw.subgroup),
            virtue        : Traits.Virtue        .get(raw.virtue),
            vice          : Traits.Vice          .get(raw.vice),

            date_created     : new Date(raw.date_created),
            date_submitted   : new Date(raw.date_submitted),
            date_approved    : new Date(raw.date_approved),
            date_last_edited : new Date(raw.date_last_edited),
        };
    },

    url: function () {
        return '/api/character/character/' + this.id ? this.id + '/' : '';
    },

    toJSON: function () {
        var attr = _.clone(this.attributes);

        attr.creature_type = attr.creature_type .id;
        attr.genealogy     = attr.genealogy     .id;
        attr.affiliation   = attr.affiliation   .id;
        attr.subgroup      = attr.subgroup      .id;
        attr.virtue        = attr.virtue        .id;
        attr.vice          = attr.vice          .id;

        attr.date_created     = attr.date_created     .toIOSString();
        attr.date_submitted   = attr.date_submitted   .toIOSString();
        attr.date_approved    = attr.date_approved    .toIOSString();
        attr.date_last_edited = attr.date_last_edited .toIOSString();

        return attr;
    },

    toHumanJSON: function () {
        var attr = _.clone(this.attributes);

        attr.creature_type = attr.creature_type .toHumanJSON();
        attr.genealogy     = attr.genealogy     .toHumanJSON();
        attr.affiliation   = attr.affiliation   .toHumanJSON();
        attr.subgroup      = attr.subgroup      .toHumanJSON();
        attr.virtue        = attr.virtue        .toHumanJSON();
        attr.vice          = attr.vice          .toHumanJSON();

        attr.date_created     = attr.date_created     .toIOSString();
        attr.date_submitted   = attr.date_submitted   .toIOSString();
        attr.date_approved    = attr.date_approved    .toIOSString();
        attr.date_last_edited = attr.date_last_edited .toIOSString();

        return attr;
    },
});

})();
