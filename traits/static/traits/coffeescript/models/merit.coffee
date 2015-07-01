###
  @file  merit.coffee
  @brief Model for character merits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.MeritType extends ORM.traits.TraitType


class ORM.traits.Merit extends ORM.traits.Trait
    @polymorphic_identity 'merit'

    defaults: () ->
        return _.extend super,
            merit_type_id          : undefined
            requires_specification : undefined
            requires_description   : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'merit_type_id'
        ORM.parse     parsed, raw, 'requires_specification'
        ORM.parse     parsed, raw, 'requires_description'

        return parsed

    @has_one 'merit_type',
        Model : ORM.traits.MeritType

    @has_many 'allowed_ratings',
        Model     : 'ORM.traits.AllowedMeritRating'
        attribute : 'merit_id'


class ORM.traits.AllowedMeritRating extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/AllowedMeritRating'

    defaults: () ->
        merit_id : undefined
        rating   : undefined

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'merit_id'
        ORM.parse.int parsed, raw, 'rating'

        return parsed

    @has_one 'merit',
        Model : ORM.traits.Merit
