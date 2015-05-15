###
  @file  power.coffee
  @brief Model for character combat traits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.PowerGroup extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/PowerGroup"

Models.PowerGroup.setup()


class Models.Power extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Power"

    defaults: () ->
        _.extends super,
            rating         : undefined
            power_group_id : undefined

    relations: [{
        type: Backbone.HasOne
        key: 'power_group'
        relatedModel: Models.PowerGroup
        includeInJSON: Models.PowerGroup.idAttribute
        autoFetch: true
        keySource: 'power_group_id'
        reverseRelationship:
            key: 'powers'
    }]

    parse: (raw) ->
        attr = super

        attr.rating         = parseInt raw.rating, 10
        attr.power_group_id = parseInt raw.power_group_id, 10

        attr.rating         = null if _.isNaN attr.rating
        attr.power_group_id = null if _.isNaN attr.power_group_id

        return attr

Models.Power.setup()
