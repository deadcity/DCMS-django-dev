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

    parse: (raw) ->
        return _.extend super,
            merit_type_id          : ORM.parse.int raw, 'merit_type_id'
            requires_specification : raw.requires_specification
            requires_description   : raw.requires_description

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

    parse: (raw) ->
        raw = super

        return {
            merit_id : ORM.parse.int raw, 'merit_id'
            rating   : ORM.parse.int raw, 'rating'
        }

ORM.traits.AllowedMeritRating.reset()

ORM.traits.AllowedMeritRating.has().one 'merit',
    model: ORM.traits.Merit
    inverse: 'allowed_ratings'

ORM.traits.Merit.has().many 'allowed_ratings',
    collection: class AllowedMeritRating_Collection extends Backbone.Collection
        model: ORM.traits.AllowedMeritRating
    inverse: 'merit'
