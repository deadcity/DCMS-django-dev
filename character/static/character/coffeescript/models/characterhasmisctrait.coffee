# DCMS auto-generated file
# 2013-09-17 09:45:58.563058

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models_NS = Tools.create_namespace 'Character.Models'

class Models_NS.CharacterHasMiscTrait extends Backbone.Model
    defaults:
        id: null
        character: null
        trait: null
        description: null
        rating: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            character: parseInt raw.character, 10
            trait: Traits.Objects.MiscTrait.get raw.trait
            description: raw.description,
            rating: parseInt raw.rating, 10
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
        "#{ DCMS.Settings.URL_PREFIX }/api/character/CharacterHasMiscTrait/#{ if @id? then "#{@id}/" else '' }"
