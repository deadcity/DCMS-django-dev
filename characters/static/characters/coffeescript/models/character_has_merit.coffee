###
  @file  character_has_merit.coffee
  @brief Model specifying the specific merit of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasMerit extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasMerit'

    defaults: () ->
        return _.extend super,
            specification : undefined
            description   : undefined

    parse: (raw) ->
        return _.extend super,
            specification : raw.specification
            description   : raw.description

Models.CharacterHasMerit.setup()
