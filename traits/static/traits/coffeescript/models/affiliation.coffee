###
  @file  affiliation.coffee
  @brief Model for character affiliations.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.Affiliation extends ORM.traits.Trait
    @parent: ORM.traits.Trait

ORM.traits.Affiliation.reset()

ORM.polymorphic_identity 'affiliation', ORM.traits.Affiliation
