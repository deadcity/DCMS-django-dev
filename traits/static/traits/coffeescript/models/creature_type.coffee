###
  @file  creature_type.coffee
  @brief Model for creature types.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.CreatureType extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/CreatureType"

    defaults: () ->
        _.extends super,
            genealogy_name   : undefined
            affiliation_name : undefined
            subgroup_name    : undefined
            power_name       : undefined

    parse: (raw) ->
        attr = super

        attr.genealogy_name   = raw.genealogy_name
        attr.affiliation_name = raw.affiliation_name
        attr.subgroup_name    = raw.subgroup_name
        attr.power_name       = raw.power_name

        return attr

Models.CreatureType.setup()
