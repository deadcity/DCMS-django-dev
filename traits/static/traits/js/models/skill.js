
(function () {

var Traits = Tools.create_namespace('Traits.Models');

var Base = Traits.Traits;

Traits.Skill = Base.extend({
    defaults: _.extend({},
        Base.prototype.defaults,
        {
            type : null,
        }
    ),

    parse: function (raw) {
        return _.extend({},
            Base.prototype.parse.apply(this, raw),
            {
                type : Traits.SkillType.get(raw.type),
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
