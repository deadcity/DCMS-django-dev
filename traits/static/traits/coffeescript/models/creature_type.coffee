###
  @file  creature_type.coffee
  @brief Model for creature types.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.CreatureType extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            genealogy_name   : undefined
            affiliation_name : undefined
            subgroup_name    : undefined
            power_name       : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'genealogy_name'
        ORM.parse parsed, raw, 'affiliation_name'
        ORM.parse parsed, raw, 'subgroup_name'
        ORM.parse parsed, raw, 'power_name'

        return parsed

ORM.traits.CreatureType.reset()

ORM.polymorphic_identity 'creature_type', ORM.traits.CreatureType
