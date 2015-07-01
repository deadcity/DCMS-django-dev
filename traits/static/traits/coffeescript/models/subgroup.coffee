###
  @file  subgroup.coffee
  @brief Model for character genealogies.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.Subgroup extends ORM.traits.Trait
    @polymorphic_identity 'subgroup'
