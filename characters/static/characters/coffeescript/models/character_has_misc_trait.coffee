###
  @file  character_has_misc_trait.coffee
  @brief Model specifying the specific miscellaneous trait of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasMiscTrait extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasMiscTrait'

    defaults: () ->
        return _.extend super,
            rating      : undefined
            description : undefined

    parse: (raw) ->
        return _.extend super,
            rating      : ORM.BaseModel.parse_int_field raw, 'rating'
            description : raw.description

Models.CharacterHasMiscTrait.setup()
