
(function () {

var Traits = Tools.create_namespace('Traits.Models');

var Base = Traits.Traits;

Traits.Flaw = Base.extend({
    defaults: _.extend({},
        Base.prototype.defaults,
        {
            requires_description : null,
        }
    ),

    parse: function (raw) {
        return _.extend({},
            Base.prototype.parse.apply(this, raw),
            {
                requires_description : raw.requires_description,
            }
        )
    },
})

})();
