###
  @file  subgroup.coffee
  @brief Model for character genealogies.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.Subgroup extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Subgroup'

Models.Subgroup.setup()
