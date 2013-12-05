# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:25 -0600 | 3f277725ac200972705ffb595dba4065

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
        character: Character.Objects.Character
        trait: Traits.Objects.Flaw.get raw.trait
        specification: raw.specification
        description: raw.description

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest
            attr.character = attr.character.toJSON options
            attr.trait = attr.trait.toJSON options

        else
            attr.character = attr.character.id
            attr.trait = attr.trait.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/character/CharacterHasFlaw/#{ if @id? then "#{ @id }/" else '' }"

