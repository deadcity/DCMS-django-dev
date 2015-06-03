###
  @file  character_has_skill.coffee
  @brief Model specifying the specific skill of a specific character.
###


Models = Tools.create_namespace 'ORM.characters'


class Models.CharacterHasSkill extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasSkill'

    defaults: () ->
        return _.extend super,
            rating : 0

    parse: (raw) ->
        return _.extend super,
            rating : ORM.BaseModel.parse_int_field raw, 'rating'

Models.CharacterHasSkill.setup()
