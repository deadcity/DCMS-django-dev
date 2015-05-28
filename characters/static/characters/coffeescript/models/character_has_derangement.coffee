###
  @file  character_has_derangement.coffee
  @brief Model specifying the specific derangement of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasDerangement extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasDerangement'

    defaults: () ->
        return _.extend super,
            specification : undefined
            description   : undefined

    parse: (raw) ->
        return _.extend super,
            specification : raw.specification
            description   : raw.description

Models.CharacterHasDerangement.setup()
