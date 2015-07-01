###
  @file  affiliation.coffee
  @brief Model for character affiliations.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.Affiliation extends ORM.traits.Trait
    @polymorphic_identity 'affiliation'
