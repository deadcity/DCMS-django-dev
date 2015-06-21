###
  @file  flaw.coffee
  @brief Model for character flaws.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.FlawType extends ORM.traits.TraitType

ORM.traits.FlawType.reset()


class ORM.traits.Flaw extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            flaw_type_id           : undefined
            requires_specification : undefined
            requires_description   : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'flaw_type_id'
        ORM.parse     parsed, raw, 'requires_specification'
        ORM.parse     parsed, raw, 'requires_description'

        return parsed

ORM.traits.Flaw.reset()

ORM.polymorphic_identity 'flaw', ORM.traits.Flaw

ORM.traits.Flaw.has().one 'flaw_type',
    model: ORM.traits.FlawType
    inverse: 'flaws'


class ORM.traits.AllowedFlawRating extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/AllowedFlawRating'

    defaults: () ->
        flaw_id : undefined
        rating  : undefined

    _parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'flaw_id'
        ORM.parse.int parsed, raw, 'rating'

        return parsed

ORM.traits.AllowedFlawRating.reset()

ORM.traits.AllowedFlawRating.has().one 'flaw',
    model: ORM.traits.Flaw
    inverse: 'allowed_ratings'

ORM.traits.Flaw.has().many 'allowed_ratings',
    collection: class AllowedFlawRating_Collection extends Backbone.Collection
        model: ORM.traits.AllowedFlawRating
    inverse: 'flaw'
