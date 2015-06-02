###
  @file  character_has_attribute.coffee
  @brief Model specifying the specific attribute of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasAttribute extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasAttribute'

    defaults: () ->
        return _.extend super,
            rating : 1

    parse: (raw) ->
        return _.extend super,
            rating : ORM.BaseModel.parse_int_field raw, 'rating'

Models.CharacterHasAttribute.setup()
