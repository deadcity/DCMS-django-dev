###
  @file  merit.coffee
  @brief Model for character merits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.MeritType extends Models.TraitType
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/MeritType"

Models.MeritType.setup()


class Models.Merit extends Models.Merit
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Merit"

    defaults: () ->
        _.extends super,
            merit_type_id          : undefined
            requires_specification : undefined
            requires_description   : undefined

    relations: [{
        type: Backbone.HasOne
        key: 'merit_type'
        relatedModel: Models.MeritType
        includeInJSON: Models.MeritType.idAttribute
        autoFetch: true
        keySource: 'merit_type_id'
    }]

    parse: (raw) ->
        attr = super

        attr.merit_type_id          = parseInt raw.merit_type_id, 10
        attr.requires_specification = raw.requires_specification
        attr.requires_description   = raw.requires_description

        attr.merit_type_id = null if _.isNaN attr.merit_type_id

        return attr

Models.Merit.setup()


class Models.AllowedMeritRating extends ORM.BaseModel
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/AllowedMeritRating"

    defaults:
        merit_id : undefined
        rating   : undefined

    relations: [{
        type: Backbone.HasOne
        key: 'merit'
        relatedModel: Models.Merit
        includeInJSON: Models.Merit.idAttribute
        autoFetch: true
        keySource: 'merit_id'
        reverseRelation:
            key: 'allowed_ratings'
    }]

Models.AllowedMeritRating.setup()
