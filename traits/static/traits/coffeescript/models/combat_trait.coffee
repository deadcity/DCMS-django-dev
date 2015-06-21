###
  @file  combat_trait.coffee
  @brief Model for character combat traits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.CombatTrait extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            rating : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed

ORM.traits.CombatTrait.reset()

ORM.polymorphic_identity 'combat_trait', ORM.traits.CombatTrait
