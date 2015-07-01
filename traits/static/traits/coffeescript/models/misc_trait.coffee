###
  @file  misc_trait.coffee
  @brief Model for character miscellaneous traits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.MiscTrait extends ORM.traits.Trait
    @polymorphic_identity 'misc_trait'

    defaults: () ->
        return _.extend super,
            requires_specification : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'requires_specification'

        return parsed
