Models_NS = Tools.create_namespace 'Character.Models'


class Models_NS.Character extends Backbone.Model
    defaults:
        id      : null
        enabled : false
        user    : null

        name          : null
        creature_type : null
        genealogy     : null
        affiliation   : null
        subgroup      : null
        virtue        : null
        vice          : null

        date_created     : null
        date_submitted   : null
        date_approved    : null
        date_last_edited : null

    parse: (raw) ->
        {
            id      : parseInt raw.id, 10
            enabled : raw.enabled
            user    : parseInt raw.id, 10

            name          : raw.name
            creature_type : Traits.Objects.CreatureType .get parseInt raw.creature_type, 10
            genealogy     : Traits.Objects.Genealogy    .get parseInt raw.genealogy,     10
            affiliation   : Traits.Objects.Affiliation  .get parseInt raw.affiliation,   10
            subgroup      : Traits.Objects.Subgroup     .get parseInt raw.subgroup,      10
            virtue        : Traits.Enums.Virtue         .get parseInt raw.virtue,        10
            vice          : Traits.Enums.Vice           .get parseInt raw.vice,          10

            date_created     : if raw.date_created?     then new Date raw.date_created     else null
            date_submitted   : if raw.date_submitted?   then new Date raw.date_submitted   else null
            date_approved    : if raw.date_approved?    then new Date raw.date_approved    else null
            date_last_edited : if raw.date_last_edited? then new Date raw.date_last_edited else null
        }

    url: () ->
        "/api/character/Character/#{ if @id? then "#{@id}/" else '' }"

    toJSON: () ->
        attr = _.clone @attributes

        attr.creature_type = attr.creature_type ?.id
        attr.genealogy     = attr.genealogy     ?.id
        attr.affiliation   = attr.affiliation   ?.id
        attr.subgroup      = attr.subgroup      ?.id
        attr.virtue        = attr.virtue        ?.valueOf()
        attr.vice          = attr.vice          ?.valueOf()

        attr.date_created     = attr.date_created     ?.toISOString()
        attr.date_submitted   = attr.date_submitted   ?.toISOString()
        attr.date_approved    = attr.date_approved    ?.toISOString()
        attr.date_last_edited = attr.date_last_edited ?.toISOString()

        return attr

    toHumanJSON: () ->
        attr = _.clone @attributes

        attr.creature_type = attr.creature_type ?.toHumanJSON()
        attr.genealogy     = attr.genealogy     ?.toHumanJSON()
        attr.affiliation   = attr.affiliation   ?.toHumanJSON()
        attr.subgroup      = attr.subgroup      ?.toHumanJSON()
        attr.virtue        = attr.virtue        ?.toString()
        attr.vice          = attr.vice          ?.toString()

        attr.date_created     = attr.date_created     ?.toISOString()
        attr.date_submitted   = attr.date_submitted   ?.toISOString()
        attr.date_approved    = attr.date_approved    ?.toISOString()
        attr.date_last_edited = attr.date_last_edited ?.toISOString()

        return attr
