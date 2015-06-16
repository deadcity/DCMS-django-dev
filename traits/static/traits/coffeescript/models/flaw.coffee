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

    parse: (raw) ->
        return _.extend super,
            flaw_type_id           : ORM.parse.int raw, 'flaw_type_id'
            requires_specification : raw.requires_specification
            requires_description   : raw.requires_description

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

    parse: (raw) ->
        raw = super

        return {
            flaw_id : ORM.parse.int raw, 'flaw_id'
            rating  : ORM.parse.int raw, 'rating'
        }

ORM.traits.AllowedFlawRating.reset()

ORM.traits.AllowedFlawRating.has().one 'flaw',
    model: ORM.traits.Flaw
    inverse: 'allowed_ratings'

ORM.traits.Flaw.has().many 'allowed_ratings',
    collection: class AllowedFlawRating_Collection extends Backbone.Collection
        model: ORM.traits.AllowedFlawRating
    inverse: 'flaw'
