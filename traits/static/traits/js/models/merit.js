
(function () {

var Traits = Tools.create_namespace('Traits.Models');

var Base = Traits.Traits;

Traits.Merit = Base.extend({
    defaults: _.extend({},
        Base.prototype.defaults,
        {
            type                   : null,
            min_rating             : null,
            max_rating             : null,
            inc_rating             : null,
            requires_specification : null,
            requires_description   : null,
        }
    ),

    parse: function (raw) {
        return _.extend({},
            Base.prototype.parse.apply(this, raw),
            {
                type                   : Traits.MeritType.get(raw.type),
                min_rating             : parseInt(raw.min_rating),
                max_rating             : parseInt(raw.max_rating),
                inc_rating             : parseInt(raw.inc_rating),
                requires_specification : raw.requires_specification,
                requires_description   : raw.requires_description,
            }
        )
    },

    toJSON: function () {
        var attr = Base.prototype.toJSON.apply(this);
        attr.type = attr.type.value();
        return attr;
    },

    toHumanJSON: function () {
        var attr = Base.prototype.toHumanJSON.apply(this);
        attr.type = attr.type.toHumanJSON();
        return attr;
    },
})

})();
