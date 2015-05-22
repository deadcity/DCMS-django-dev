###
  @file  power.coffee
  @brief Model for character combat traits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.PowerGroup extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/PowerGroup'

Models.PowerGroup.setup()


class Models.Power extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/Power'

    defaults: () ->
        return _.extend super,
            rating         : undefined
            power_group_id : undefined

    relations: [
        type: Backbone.HasOne
        key: 'power_group'
        relatedModel: Models.PowerGroup
        includeInJSON: Models.PowerGroup.idAttribute
        autoFetch: true
        keySource: 'power_group_id'
        reverseRelationship:
            key: 'powers'
    ]

    parse: (raw) ->
        return _.extend super,
            rating         : ORM.BaseModel.parse_int_field raw, 'rating'
            power_group_id : ORM.BaseModel.parse_int_field raw, 'power_group_id'

Models.Power.setup()
