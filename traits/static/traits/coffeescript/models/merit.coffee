###
  @file  merit.coffee
  @brief Model for character merits.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.MeritType extends Models.TraitType
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/MeritType'

Models.MeritType.setup()


class Models.Merit extends Models.Merit
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/Merit'

    defaults: () ->
        return _.extend super,
            merit_type_id          : undefined
            requires_specification : undefined
            requires_description   : undefined

    relations: [
        type: Backbone.HasOne
        key: 'merit_type'
        relatedModel: Models.MeritType
        includeInJSON: Models.MeritType.idAttribute
        autoFetch: true
        keySource: 'merit_type_id'
    ]

    parse: (raw) ->
        return _.extend super,
            merit_type_id          : ORM.BaseModel.parse_int_field raw, 'merit_type_id'
            requires_specification : raw.requires_specification
            requires_description   : raw.requires_description

Models.Merit.setup()


class Models.AllowedMeritRating extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/AllowedMeritRating'

    defaults: () ->
        merit_id : undefined
        rating   : undefined

    relations: [
        type: Backbone.HasOne
        key: 'merit'
        relatedModel: Models.Merit
        includeInJSON: Models.Merit.idAttribute
        autoFetch: true
        keySource: 'merit_id'
        reverseRelation:
            key: 'allowed_ratings'
    ]

    parse: (raw) ->
        merit_id : ORM.BaseModel.parse_int_field raw, 'merit_id'
        rating   : ORM.BaseModel.parse_int_field raw, 'rating'

Models.AllowedMeritRating.setup()
