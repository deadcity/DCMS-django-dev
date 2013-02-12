
(function () {

var Traits = Tools.create_namespace('Traits.Models');

var Base = Traits.Traits;

Traits.Flaw = Base.extend({
    defaults: _.extend({},
        Base.prototype.defaults,
        {
            type                    : null,
            requires_specification  : null,
            requires_description    : null,
        }
    ),

    parse: function (raw) {
        return _.extend({},
            Base.prototype.parse.apply(this, raw),
            {
                type                   : Traits.FlawType.get(raw.type),
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
