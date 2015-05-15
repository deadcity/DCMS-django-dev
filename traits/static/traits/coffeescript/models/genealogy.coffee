###
  @file  genealogy.coffee
  @brief Model for character genealogies.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.Genealogy extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Genealogy"

Models.Genealogy.setup()
