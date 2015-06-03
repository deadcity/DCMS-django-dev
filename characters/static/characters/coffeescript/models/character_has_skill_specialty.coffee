###
  @file  character_has_skill_specialty.coffee
  @brief Model specifying the specific skill specialty of a specific character.
###


Models = Tools.create_namespace 'ORM.characters'


class Models.CharacterHasSkillSpecialty extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasSkillSpecialty'

    defaults: () ->
        return _.extend super,
            specialty : undefined

    parse: (raw) ->
        return _.extend super,
            specialty : raw.specialty

Models.CharacterHasSkillSpecialty.setup()
