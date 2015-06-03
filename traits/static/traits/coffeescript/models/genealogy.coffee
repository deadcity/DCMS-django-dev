###
  @file  genealogy.coffee
  @brief Model for character genealogies.
###


Models = Tools.create_namespace 'ORM.traits'


class Models.Genealogy extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Genealogy'

Models.Genealogy.setup()
