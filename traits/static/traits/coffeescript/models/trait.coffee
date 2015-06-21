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

    _parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'

        ORM.parse.int parsed, raw, 'chronicle_id'

        ORM.parse parsed, raw, 'name'
        ORM.parse parsed, raw, 'label'

        return parsed

ORM.traits.TraitType.reset()

ORM.traits.TraitType.has().one 'chronicle',
    model: ORM.chronicles.ChronicleBase
    inverse: 'trait_types'


class ORM.traits.Trait extends ORM.BaseModel
    @_polymorphic_on: 'trait_type'
    @_polymorphic_identity: {}

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/' + @constructor.name

    defaults: () ->
        id         : undefined
        trait_type : undefined

        chronicle_id : undefined

        name  : undefined
        label : ''
        order : undefined

    _parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'
        ORM.parse     parsed, raw, trait_type

        ORM.parse.int parsed, raw, 'chronicle_id'

        ORM.parse     parsed, raw, name
        ORM.parse     parsed, raw, label
        ORM.parse.int parsed, raw, 'order'

        return parsed

ORM.traits.Trait.reset()

ORM.traits.Trait.has().one 'chronicle',
    model: ORM.chronicles.ChronicleBase
    inverse: 'traits'

ORM.chronicles.ChronicleBase.has().many 'traits',
    collection: class Trait_Collection extends Backbone.Collection
        model: ORM.traits.Trait
    inverse: 'chronicle'
