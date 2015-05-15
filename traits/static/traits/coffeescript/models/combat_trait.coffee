###
  @file  combat_trait.coffee
  @brief Model for character combat traits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.CombatTrait extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/CombatTrait"

    defaults: () ->
        _.extends super,
            rating : undefined

    parse: (raw) ->
        attr = super

        attr.rating: parseInt raw.rating, 10

        attr.rating = null if _.isNaN attr.rating

        return attr

Models.CombatTrait.setup()
