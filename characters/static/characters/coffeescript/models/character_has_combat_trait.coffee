###
  @file  character_has_combat_trait.coffee
  @brief Model specifying the specific combat-trait of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasCombatTrait extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasCombatTrait'

    defaults: () ->
        return _.extend super,
            rating : undefined

    parse: (raw) ->
        return _.extend super,
            rating : ORM.BaseModel.parse_int_field raw, 'rating'

Models.CharacterHasCombatTrait.setup()
