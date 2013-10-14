# DCMS auto-generated file
# 2013-10-14 12:00:06.268298

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models_NS = Tools.create_namespace 'Character.Models'

class Models_NS.XPRecord extends Backbone.Model
    defaults:
        id: null
        character: null
        amount: null
        note: null
        game: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            character: parseInt raw.character, 10
            amount: parseInt raw.amount, 10
            note: raw.note,
            game: Chronicle.Objects.Game.get raw.game
        }

    toJSON: () ->
        attr = _.clone this.attributes
        attr.game = attr.game.id
        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes
        attr.game = attr.game.toHumanJSON()
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/character/XPRecord/#{ if @id? then "#{@id}/" else '' }"
