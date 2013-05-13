// DCMS auto-generated file
// 2013-05-13 11:58:31.554397

/* * * * * * * * * * * * * * * * * * * * * * *
 * DO NOT MODIFY THE CONTENTS OF THIS FILE!  *
 * * * * * * * * * * * * * * * * * * * * * * */

// If you wish to alter it's contents modify either the source model, or the
// generating tool and then run `manage.py generate_classes` again.  (Don't
// forget to commit the newly generated files!)


(function () {

var Models = Tools.create_namespace('Character.Models');

Models.CharacterHasSkill = Backbone.Model.extend({
    defaults: {
        id: null,
        character: null,
        trait: null,
        rating: null,
    },

    parse: function (raw) {
        return {
            id: parseInt(raw.id, 10),
            character: parseInt(raw.character, 10),
            trait: Traits.Objects.Skill.get(parseInt(raw.trait, 10)),
            rating: parseInt(raw.rating, 10),
        }
    },

    toJSON: function () {
        var attr = _.clone(this.attributes);
        attr.trait = attr.trait.id;
        return attr;
    },

    toHumanJSON: function () {
        var attr = _.clone(this.attributes);
        attr.trait = attr.trait.toHumanJSON();
        return attr;
    },

    url: function () {
        return '/api/character/CharacterHasSkill/' + (this.id == null ? '' : this.id + '/');
    },
});

})();
