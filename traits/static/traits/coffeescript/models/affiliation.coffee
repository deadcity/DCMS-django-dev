###
  @file  affiliation.coffee
  @brief Model for character affiliations.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.Affiliation extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Affiliation"

Models.Affiliation.setup()
