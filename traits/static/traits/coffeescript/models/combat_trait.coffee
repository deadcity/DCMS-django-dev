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
        return _.extend super,
            rating : ORM.parse.int raw, 'rating'

ORM.traits.CombatTrait.reset()

ORM.polymorphic_identity 'combat_trait', ORM.traits.CombatTrait
