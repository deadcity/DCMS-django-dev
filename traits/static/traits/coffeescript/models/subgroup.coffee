###
  @file  subgroup.coffee
  @brief Model for character genealogies.
###


Models = Tools.create_namespace 'ORM.traits'


class Models.Subgroup extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Subgroup'

Models.Subgroup.setup()
