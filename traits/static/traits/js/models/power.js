
(function () {

var Traits = Tools.create_namespace('Traits.Models');

var Base = Traits.Traits;

Traits.Power = Base.extend({
    defaults: _.extend({},
        Base.prototype.defaults,
        {
            rating : null,
            group  : null,
        }
    ),

    parse: function (raw) {
        return _.extend({},
            Base.prototype.parse.apply(this, raw),
            {
                rating : parseInt(raw.rating),
                group  : raw.group,
            }
        )
    },
})

})();
