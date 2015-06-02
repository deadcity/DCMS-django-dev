###
  @file  game.coffee
  @brief Models for game objects.
###


Models = Tools.create_namespace 'ORM.Chronicles'


class Models.Game extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/Game'

    defaults: () ->
        id : undefined

        enabled : true

        name         : undefined
        chronicle_id : undefined
        date         : undefined

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        enabled : raw.enabled

        name         : raw.name
        chronicle_id : ORM.BaseModel.parse_int_field raw, 'chronicle_id'
        date         : ORM.BaseModel.parse_date_field raw, 'date'

Models.Game.setup()
