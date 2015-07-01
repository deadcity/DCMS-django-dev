###
  @file  trait.coffee
  @brief Base models for traits and trait-types.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.TraitType extends ORM.BaseModel
    urlRoot: () ->
        return undefined if @constructor is ORM.traits.TraitType
        return DCMS.Settings.URL_PREFIX + '/rest/traits/' + @constructor.name

    defaults: () ->
        id : undefined

        chronicle_id : undefined

        name  : undefined
        label : ''

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'

        ORM.parse.int parsed, raw, 'chronicle_id'

        ORM.parse parsed, raw, 'name'
        ORM.parse parsed, raw, 'label'

        return parsed

    @has_one 'chronicle',
        Model : ORM.chronicles.ChronicleBase


class ORM.traits.Trait extends ORM.BaseModel
    @polymorphic_on 'trait_type'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/' + @constructor.name

    defaults: () ->
        id         : undefined
        trait_type : undefined

        chronicle_id : undefined

        name  : undefined
        label : ''
        order : undefined

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'
        ORM.parse     parsed, raw, 'trait_type'

        ORM.parse.int parsed, raw, 'chronicle_id'

        ORM.parse     parsed, raw, 'name'
        ORM.parse     parsed, raw, 'label'
        ORM.parse.int parsed, raw, 'order'

        return parsed

    @has_one 'chronicle',
        Model : ORM.chronicles.ChronicleBase
