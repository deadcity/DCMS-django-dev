###
  @file  misc_trait.coffee
  @brief Model for character miscellaneous traits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.MiscTrait extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/MiscTrait'

    defaults: () ->
        return _.extend super,
            requires_specification : undefined

    parse: (raw) ->
        return _.extend super,
            requires_specification : raw.requires_specification

Models.MiscTrait.setup()
