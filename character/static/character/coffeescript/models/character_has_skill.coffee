# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:40 -0600 | e01dc1dff67f9eb5e2ebe4908f9b757d

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Character.Models'


class Models.CharacterHasSkill extends Backbone.Model
    defaults:
        id: null
        character: null
        trait: null
        rating: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        character: Character.Objects.Character
        trait: Traits.Objects.Skill.get raw.trait
        rating: parseInt raw.rating, 10

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
        "#{ DCMS.Settings.URL_PREFIX }/api/character/CharacterHasSkill/#{ if @id? then "#{ @id }/" else '' }"

