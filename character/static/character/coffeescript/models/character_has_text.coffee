# DCMS auto-generated file
# Thu, 5 Dec 2013 10:37:53 -0600 | 2c6f055466d7c8f9f650c2302d9412d7

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
            attr.trait = attr.trait.toJSON options

        else
            attr.trait = attr.trait.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/character/CharacterHasText/#{ if @id? then "#{ @id }/" else '' }"

