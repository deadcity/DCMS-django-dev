###
  @file  affiliation.coffee
  @brief Model for character affiliations.
###


Models = Tools.create_namespace 'ORM.traits'


class Models.Affiliation extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Affiliation'

Models.Affiliation.setup()
