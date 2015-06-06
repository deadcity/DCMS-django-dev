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

    parse: (raw) ->
        return _.extend super,
            requires_specification : raw.requires_specification

ORM.traits.MiscTrait.reset()

ORM.polymorphic_identity 'misc_trait', ORM.traits.MiscTrait
