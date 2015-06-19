###
  @file  game.coffee
  @brief Models for game objects.
###


Tools.create_namespace 'ORM.chronicles'


class ORM.chronicles.Game extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/Game'

    defaults: () ->
        id : undefined

        enabled : true

        name         : undefined
        chronicle_id : undefined
        date         : undefined

    _parse: (raw) ->
        raw = super

        return {
            id : ORM.parse.int raw, 'id'

            enabled : raw.enabled

            name         : raw.name
            chronicle_id : ORM.parse.int raw, 'chronicle_id'
            date         : ORM.parse.date raw, 'date'
        }

ORM.chronicles.Game.reset()

ORM.chronicles.Game.has().one 'chronicle',
    model: ORM.chronicles.Chronicle
    inverse: 'games'

ORM.chronicles.Chronicle.has().many 'games',
    collection: class Game_Collection extends Backbone.Collection
        model: ORM.chronicles.Game
    inverse: 'chronicle'
