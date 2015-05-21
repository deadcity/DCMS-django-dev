###
  @file  character.coffee
  @brief Model for character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.Character extends ORM.BaseModel
    @Status: new Tools.Enum [
        { name: 'EDITING',   value: 1 }
        { name: 'SUBMITTED', }
        { name: 'APPROVED',  }
        { name: 'ACTIVE',    }
        { name: 'DECEASED',  }
        { name: 'INACTIVE',  }
    ]

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/Character'

    defaults: () ->
        id : undefined

        enabled      : true
        user_id      : undefined
        # chronicle_id : undefined
        status       : Character.Status.EDITING

        name             : undefined
        creature_type_id : undefined
        genealogy_id     : undefined
        affiliation_id   : undefined
        subgroup_id      : undefined
        virtue_id        : undefined
        vice_id          : undefined

        date_created     : undefined
        date_submitted   : undefined
        date_approved    : undefined
        date_last_edited : undefined

    relations: [
        # User
        type: Backbone.HasOne
        key: 'user'
        relatedModel: ORM.Auth.User
        includeInJSON: ORM.Auth.User.idAttribute
        autoFetch: true
        keySource: 'user_id'
    ,
        # Chronicle
        type: Backbone.HasOne
        key: 'chronicle'
        relatedModel: ORM.Chronicle.Chronicle
        includeInJSON: ORM.Chronicle.Chronicle.idAttribute
        autoFetch: true
        keySource: 'chronicle_id'
    ,
        # Crature Type
        type: Backbone.HasOne
        key: 'creature_type'
        relatedModel: ORM.Traits.CreatureType
        includeInJSON: ORM.Traits.CreatureType.idAttribute
        autoFetch: true
        keySource: 'creature_type_id'
    ,
        # Genealogy
        type: Backbone.HasOne
        key: 'genealogy'
        relatedModel: ORM.Traits.Genealogy
        includeInJSON: ORM.Traits.Genealogy.idAttribute
        autoFetch: true
        keySource: 'genealogy_id'
    ,
        # Affiliation
        type: Backbone.HasOne
        key: 'affiliation'
        relatedModel: ORM.Traits.Affiliation
        includeInJSON: ORM.Traits.Affiliation.idAttribute
        autoFetch: true
        keySource: 'affiliation_id'
    ,
        # Subgroup
        type: Backbone.HasOne
        key: 'subgroup'
        relatedModel: ORM.Traits.Subgroup
        includeInJSON: ORM.Traits.Subgroup.idAttribute
        autoFetch: true
        keySource: 'subgroup_id'
    ,
        # Virtue
        type: Backbone.HasOne
        key: 'virtue'
        relatedModel: ORM.Traits.Virtue
        includeInJSON: ORM.Traits.Virtue.idAttribute
        autoFetch: true
        keySource: 'virtue_id'
    ,
        # Vice
        type: Backbone.HasOne
        key: 'vice'
        relatedModel: ORM.Traits.Vice
        includeInJSON: ORM.Traits.Vice.idAttribute
        autoFetch: true
        keySource: 'vice_id'
    ]

    parse: (raw) ->
        attr =
            id : parseInt raw.id, 10

            enabled      : raw.enabled
            user_id      : parseInt raw.user, 10
            # chronicle_id : Chronicle.Objects.Chronicle .get parseInt raw.chronicle, 10
            status       : Character.Status.get raw.status

            name             : raw.name
            creature_type_id : parseInt raw.creature_type_id, 10
            genealogy_id     : parseInt raw.genealogy_id,     10
            affiliation_id   : parseInt raw.affiliation_id,   10
            subgroup_id      : parseInt raw.subgroup_id,      10
            virtue_id        : parseInt raw.virtue_id,        10
            vice_id          : parseInt raw.vice_id,          10

            date_created     : if raw.date_created?     then new Date raw.date_created     else null
            date_submitted   : if raw.date_submitted?   then new Date raw.date_submitted   else null
            date_approved    : if raw.date_approved?    then new Date raw.date_approved    else null
            date_last_edited : if raw.date_last_edited? then new Date raw.date_last_edited else null

        attr.user_id = null if _.isNaN attr.user_id

        attr.creature_type_id = null if _.isNaN attr.creature_type_id
        attr.genealogy_id     = null if _.isNaN attr.genealogy_id
        attr.affiliation_id   = null if _.isNaN attr.affiliation_id
        attr.subgroup_id      = null if _.isNaN attr.subgroup_id
        attr.virtue_id        = null if _.isNaN attr.virtue_id
        attr.vice_id          = null if _.isNaN attr.vice_id

        attr.date_created     = null if _.isNaN attr.date_created
        attr.date_submitted   = null if _.isNaN attr.date_submitted
        attr.date_approved    = null if _.isNaN attr.date_approved
        attr.date_last_edited = null if _.isNaN attr.date_last_edited

        return attr

Models.Character.setup()
