# DCMS auto-generated file
# 2013-09-10 11:58:03.321986

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models_NS = Tools.create_namespace 'Character.Models'

class Models_NS.CharacterHasPower extends Backbone.Model
    defaults:
        id: null
        character: null
        trait: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            character: parseInt raw.character, 10
            trait: Traits.Objects.Power.get parseInt raw.trait, 10
        }

    toJSON: () ->
        attr = _.clone this.attributes
        attr.trait = attr.trait.id
        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes
        attr.trait = attr.trait.toHumanJSON()
        attr

    url: () ->
        "/api/character/CharacterHasPower/#{ if @id? then "#{@id}/" else '' }"
