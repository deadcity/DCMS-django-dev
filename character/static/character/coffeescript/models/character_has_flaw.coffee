# DCMS auto-generated file
# Thu, 14 Nov 2013 16:56:15 -0600 | 224b0d6f08ecd87dda1d83cad699aa75

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Character.Models'


class Models.CharacterHasFlaw extends Backbone.Model
    defaults:
        id: null
        character: null
        trait: null
        specification: null
        description: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        character: parseInt raw.character, 10
        trait: raw.trait
        specification: raw.specification
        description: raw.description

    toJSON: () ->
        attr = _.clone @attributes
        attr.character = attr.character.id
        attr.trait = attr.trait.id
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
        attr.character = attr.character.toHumanJSON()
        attr.trait = attr.trait.toHumanJSON()
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/character/CharacterHasFlaw/#{ if @id? then "#{ @id }/" else '' }"

