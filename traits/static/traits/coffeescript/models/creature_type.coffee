###
  @file  creature_type.coffee
  @brief Model for creature types.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.CreatureType extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/CreatureType'

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

Models.CreatureType.setup()
