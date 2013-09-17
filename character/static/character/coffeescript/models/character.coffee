Models_NS = Tools.create_namespace 'Character.Models'


class Models_NS.Character extends Backbone.Model
    defaults:
        id      : null
        enabled : false
        user    : null

        # chronicle : null
        # status : null

        name          : null
        status        : null
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
            status        : Traits.Enums.Status         .get parseInt raw.status,        10
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

        attr.creature_type = attr.creature_type ?.toHumanJSON() ? new Object()
        attr.genealogy     = attr.genealogy     ?.toHumanJSON() ? new Object()
        attr.affiliation   = attr.affiliation   ?.toHumanJSON() ? new Object()
        attr.subgroup      = attr.subgroup      ?.toHumanJSON() ? new Object()
        attr.virtue        = attr.virtue        ? new Object()
        attr.vice          = attr.vice          ? new Object()

        attr.date_created     = attr.date_created     ?.toISOString() ? new Object()
        attr.date_submitted   = attr.date_submitted   ?.toISOString() ? new Object()
        attr.date_approved    = attr.date_approved    ?.toISOString() ? new Object()
        attr.date_last_edited = attr.date_last_edited ?.toISOString() ? new Object()

        return attr
