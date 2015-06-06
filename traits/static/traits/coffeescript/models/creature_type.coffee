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

    parse: (raw) ->
        return _.extend super,
            genealogy_name   : raw.genealogy_name
            affiliation_name : raw.affiliation_name
            subgroup_name    : raw.subgroup_name
            power_name       : raw.power_name

ORM.traits.CreatureType.reset()

ORM.polymorphic_identity 'creature_type', ORM.traits.CreatureType
