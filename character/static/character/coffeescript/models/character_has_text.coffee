# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:26 -0600 | 5026cb81f41ba1d7f1f3f75a3b19ea3b

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Character.Models'


class Models.CharacterHasText extends Backbone.Model
    defaults:
        id: null
        character: null
        trait: null
        text: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        character: Character.Objects.Character
        trait: Traits.Objects.CharacterText.get raw.trait
        text: raw.text

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
        "#{ DCMS.Settings.URL_PREFIX }/character/CharacterHasText/#{ if @id? then "#{ @id }/" else '' }"

