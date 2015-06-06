###
  @file  subgroup.coffee
  @brief Model for character genealogies.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.Subgroup extends ORM.traits.Trait
    @parent: ORM.traits.Trait

ORM.traits.Subgroup.reset()

ORM.polymorphic_identity 'subgroup', ORM.traits.Subgroup
