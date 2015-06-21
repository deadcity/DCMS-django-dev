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
        parsed = {}

        ORM.parse.int parsed, raw, 'id'

        ORM.parse parsed, raw, 'enabled'

        ORM.parsed     parsed, raw, 'name'
        ORM.parse.int  parsed, raw, 'chronicle_id'
        ORM.parse.date parsed, raw, 'date'

        return parsed

ORM.chronicles.Game.reset()

ORM.chronicles.Game.has().one 'chronicle',
    model: ORM.chronicles.Chronicle
    inverse: 'games'

ORM.chronicles.Chronicle.has().many 'games',
    collection: class Game_Collection extends Backbone.Collection
        model: ORM.chronicles.Game
    inverse: 'chronicle'
