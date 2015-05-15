###
  @file  misc_trait.coffee
  @brief Model for character miscellaneous traits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.MiscTrait extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/MiscTrait"

    defaults: () ->
        _.extends super,
            requires_specification : undefined

    parse: (raw) ->
        attr = super

        attr.requires_specification = raw.requires_specification

        return attr

Models.MiscTrait.setup()
