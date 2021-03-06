###
  @file  character_combat_trait.coffee
  @brief Model specifying the specific combat-trait of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterCombatTrait extends ORM.characters.CharacterTrait
    @polymorphic_identity 'combat_trait'

    defaults: () ->
        return _.extend super,
            rating : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed
