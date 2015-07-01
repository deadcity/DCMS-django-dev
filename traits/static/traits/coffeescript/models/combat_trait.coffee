###
  @file  combat_trait.coffee
  @brief Model for character combat traits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.CombatTrait extends ORM.traits.Trait
    @polymorphic_identity 'combat_trait'

    defaults: () ->
        return _.extend super,
            rating : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed
