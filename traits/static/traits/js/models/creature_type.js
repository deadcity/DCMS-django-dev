
(function () {

var Traits = Tools.create_namespace('Traits.Models');

var Base = Traits.Traits;

Traits.CreatureType = Base.extend({
    defaults: _.extend({},
        Base.prototype.defaults,
        {
            genealogy_name   : null,
            affiliation_name : null,
            subgroup_name    : null,
            power_name       : null,
        }
    ),

    parse: function (raw) {
        return _.extend({},
            Base.prototype.parse.apply(this, raw),
            {
                genealogy_name   : raw.genealogy_name,
                affiliation_name : raw.affiliation_name,
                subgroup_name    : raw.subgroup_name,
                power_name       : raw.power_name,
            }
        )
    },
})

})();
