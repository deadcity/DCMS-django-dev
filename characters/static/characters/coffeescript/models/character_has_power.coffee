###
  @file  character_has_power.coffee
  @brief Model specifying the specific power of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasPower extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasPower'

Models.CharacterHasPower.setup()
