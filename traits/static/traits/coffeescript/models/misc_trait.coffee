###
  @file  misc_trait.coffee
  @brief Model for character miscellaneous traits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.MiscTrait extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            requires_specification : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'requires_specification'

        return parsed

ORM.traits.MiscTrait.reset()

ORM.polymorphic_identity 'misc_trait', ORM.traits.MiscTrait
