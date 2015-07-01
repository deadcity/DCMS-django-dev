###
  @file  genealogy.coffee
  @brief Model for character genealogies.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.Genealogy extends ORM.traits.Trait
    @polymorphic_identity 'genealogy'
