###
  @file  power.coffee
  @brief Model for character combat traits.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.PowerGroup extends ORM.traits.Trait
    @polymorphic_identity 'power_group'

    @has_many 'powers',
        Model     : 'ORM.traits.Power'
        attribute : 'power_group_id'


class ORM.traits.Power extends ORM.traits.Trait
    @polymorphic_identity 'power'

    defaults: () ->
        return _.extend super,
            rating         : undefined
            power_group_id : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'
        ORM.parse.int parsed, raw, 'power_group_id'

        return parsed

    @has_one 'power_group',
        Model: ORM.traits.PowerGroup
