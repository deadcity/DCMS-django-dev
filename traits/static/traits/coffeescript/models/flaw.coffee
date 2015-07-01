###
  @file  flaw.coffee
  @brief Model for character flaws.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.FlawType extends ORM.traits.TraitType


class ORM.traits.Flaw extends ORM.traits.Trait
    @polymorphic_identity 'flaw'

    defaults: () ->
        return _.extend super,
            flaw_type_id           : undefined
            requires_specification : undefined
            requires_description   : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'flaw_type_id'
        ORM.parse     parsed, raw, 'requires_specification'
        ORM.parse     parsed, raw, 'requires_description'

        return parsed

    @has_one 'flaw_type',
        Model : ORM.traits.FlawType

    @has_many 'allowed_ratings',
        Model     : 'ORM.traits.AllowedFlawRating'
        attribute : 'flaw_id'


class ORM.traits.AllowedFlawRating extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/AllowedFlawRating'

    defaults: () ->
        flaw_id : undefined
        rating  : undefined

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'flaw_id'
        ORM.parse.int parsed, raw, 'rating'

        return parsed

    @has_one 'flaw',
        Model : ORM.traits.Flaw
