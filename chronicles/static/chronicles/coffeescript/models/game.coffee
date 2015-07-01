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

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'

        ORM.parse parsed, raw, 'enabled'

        ORM.parsed     parsed, raw, 'name'
        ORM.parse.int  parsed, raw, 'chronicle_id'
        ORM.parse.date parsed, raw, 'date'

        return parsed

    @has_one 'chronicle',
        Model : ORM.chronicles.Chronicle
