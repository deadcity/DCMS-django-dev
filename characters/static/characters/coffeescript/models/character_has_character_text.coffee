###
  @file  character_has_character_text.coffee
  @brief Model specifying the specific text of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasCharacterText extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasCharacterText'

    defaults: () ->
        return _.extend super,
            text : undefined

    parse: (raw) ->
        return _.extend super,
            text : raw.text

Models.CharacterHasCharacterText.setup()
