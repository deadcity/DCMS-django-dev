# DCMS auto-generated file
# Thu, 5 Dec 2013 10:37:53 -0600 | c26c6d44be7b14979d3a0085e8c1cd55

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Character.Models'


class Models.XPRecord extends Backbone.Model
    defaults:
        id: null
        game: null
        character: null
        amount: null
        note: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        game: Chronicle.Objects.Game.get raw.game
        character: Character.Objects.Character
        amount: parseInt raw.amount, 10
        note: raw.note

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest
            attr.game = attr.game.toJSON options

        else
            attr.game = attr.game.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/character/XPRecord/#{ if @id? then "#{ @id }/" else '' }"

