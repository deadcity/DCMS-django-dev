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
        raw = super

        return {
            id : ORM.parse.int raw, 'id'

            chronicle_id : ORM.parse.int raw, 'chronicle_id'

            name  : raw.name
            label : raw.label
        }

ORM.traits.TraitType.reset()

ORM.traits.TraitType.has().one 'chronicle',
    model: ORM.chronicles.ChronicleBase
    inverse: 'trait_types'


class ORM.traits.Trait extends ORM.BaseModel
    @_polymorphic_on: '_discriminator'
    @_polymorphic_identity: {}

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/' + @constructor.name

    defaults: () ->
        id             : undefined
        _discriminator : undefined

        chronicle_id : undefined

        name  : undefined
        label : ''
        order : undefined

    parse: (raw) ->
        raw = super

        return {
            id             : ORM.parse.int raw, 'id'
            _discriminator : raw._discriminator

            chronicle_id : ORM.parse.int raw, 'chronicle_id'

            name  : raw.name
            label : raw.label
            order : ORM.parse.int raw, 'order'
        }

ORM.traits.Trait.reset()

ORM.traits.Trait.has().one 'chronicle',
    model: ORM.chronicles.ChronicleBase
    inverse: 'traits'

ORM.chronicles.ChronicleBase.has().many 'traits',
    collection: class Trait_Collection extends Backbone.Collection
        model: ORM.traits.Trait
    inverse: 'chronicle'
