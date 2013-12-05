# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:26 -0600 | 2ef6bc289ccc04322b74a0d31e1831bc

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Character.Models'


class Models.CharacterHasSkillSpecialty extends Backbone.Model
    defaults:
        id: null
        character: null
        trait: null
        specialty: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        character: Character.Objects.Character
        trait: Traits.Objects.Skill.get raw.trait
        specialty: raw.specialty

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
        "#{ DCMS.Settings.URL_PREFIX }/character/CharacterHasSkillSpecialty/#{ if @id? then "#{ @id }/" else '' }"

