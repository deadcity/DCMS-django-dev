###
  @file  character_has_combat_trait.coffee
  @brief Model specifying the specific combat-trait of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasCombatTrait extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            rating : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed

ORM.characters.CharacterHasCombatTrait.reset()

ORM.polymorphic_identity 'combat_trait', ORM.characters.CharacterHasCombatTrait

ORM.characters.CharacterHasCombatTrait.has().one 'trait',
    model: ORM.traits.CombatTrait
    inverse: 'character_has_combat_trait'

ORM.characters.CharacterHasCombatTrait.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_combat_traits'

ORM.characters.Character.has().many 'character_combat_traits',
    collection: class CharacterHasCombatTrait_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasCombatTrait
    inverse: 'character'
