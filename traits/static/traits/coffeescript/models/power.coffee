###
  @file  power.coffee
  @brief Model for character combat traits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.PowerGroup extends ORM.traits.Trait
    @parent: ORM.traits.Trait

ORM.traits.PowerGroup.reset()

ORM.polymorphic_identity 'power_group', ORM.traits.PowerGroup


class ORM.traits.Power extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            rating         : undefined
            power_group_id : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'
        ORM.parse.int parsed, raw, 'power_group_id'

        return parsed

ORM.traits.Power.reset()

ORM.polymorphic_identity 'power', ORM.traits.Power

ORM.traits.Power.has().one 'power_group',
    model: ORM.traits.PowerGroup
    inverse: 'powers'

ORM.traits.PowerGroup.has().many 'powers',
    collection: class Power_Collection extends Backbone.Collection
        model: ORM.traits.Power
    inverse: 'power_group'
