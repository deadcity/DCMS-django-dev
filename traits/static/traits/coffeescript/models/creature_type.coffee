###
  @file  creature_type.coffee
  @brief Model for creature types.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.CreatureType extends ORM.traits.Trait
    @polymorphic_identity 'creature_type'

    defaults: () ->
        return _.extend super,
            genealogy_name   : undefined
            affiliation_name : undefined
            subgroup_name    : undefined
            power_name       : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'genealogy_name'
        ORM.parse parsed, raw, 'affiliation_name'
        ORM.parse parsed, raw, 'subgroup_name'
        ORM.parse parsed, raw, 'power_name'

        return parsed
