###
  @file  character_has_flaw.coffee
  @brief Model specifying the specific flaw of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasFlaw extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasFlaw'

    defaults: () ->
        return _.extend super,
            specification : undefined
            description   : undefined

    parse: (raw) ->
        return _.extend super,
            specification : raw.specification
            description   : raw.description

Models.CharacterHasFlaw.setup()
