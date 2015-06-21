###
  @file  merit.coffee
  @brief Model for character merits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.MeritType extends ORM.traits.TraitType

ORM.traits.MeritType.reset()


class ORM.traits.Merit extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            merit_type_id          : undefined
            requires_specification : undefined
            requires_description   : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'merit_type_id'
        ORM.parse     parsed, raw, 'requires_specification'
        ORM.parse     parsed, raw, 'requires_description'

        return parsed

ORM.traits.Merit.reset()

ORM.polymorphic_identity 'merit', ORM.traits.Merit

ORM.traits.Merit.has().one 'merit_type',
    model: ORM.traits.MeritType
    inverse: 'merits'


class ORM.traits.AllowedMeritRating extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/AllowedMeritRating'

    defaults: () ->
        merit_id : undefined
        rating   : undefined

    _parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'merit_id'
        ORM.parse.int parsed, raw, 'rating'

        return parsed

ORM.traits.AllowedMeritRating.reset()

ORM.traits.AllowedMeritRating.has().one 'merit',
    model: ORM.traits.Merit
    inverse: 'allowed_ratings'

ORM.traits.Merit.has().many 'allowed_ratings',
    collection: class AllowedMeritRating_Collection extends Backbone.Collection
        model: ORM.traits.AllowedMeritRating
    inverse: 'merit'
