###
  @file  combat_trait.coffee
  @brief Model for character combat traits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.CombatTrait extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/CombatTrait'

    defaults: () ->
        return _.extend super,
            rating : undefined

    parse: (raw) ->
        return _.extend super,
            rating : ORM.BaseModel.parse_int_field raw, 'rating'

Models.CombatTrait.setup()
