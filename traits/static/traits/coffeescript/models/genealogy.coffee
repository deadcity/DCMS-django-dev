###
  @file  genealogy.coffee
  @brief Model for character genealogies.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.Genealogy extends ORM.traits.Trait
    @parent: ORM.traits.Trait

ORM.traits.Genealogy.reset()

ORM.polymorphic_identity 'genealogy', ORM.traits.Genealogy
