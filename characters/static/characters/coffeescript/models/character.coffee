###
  @file  character.coffee
  @brief Model for character.
###


Models = Tools.create_namespace 'ORM.Characters'


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
        DCMS.Settings.URL_PREFIX + '/characters/Character'

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
    #     # Chronicle
    #     type: Backbone.HasOne
    #     key: 'chronicle'
    #     relatedModel: ORM.Chronicle.Chronicle
    #     includeInJSON: ORM.Chronicle.Chronicle.idAttribute
    #     autoFetch: true
    #     keySource: 'chronicle_id'
    # ,

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
    ,

        # Attributes
        type: Backbone.HasMany
        key: 'attributes'
        relatedModel: ORM.Characters.CharacterHasAttribute
        includeInJSON: false
    ,
        # Skills
        type: Backbone.HasMany
        key: 'skills'
        relatedModel: ORM.Characters.CharacterHasSkill
        includeInJSON: false
    ,
        # Skil Specialties
        type: Backbone.HasMany
        key: 'skill_specialties'
        relatedModel: ORM.Characters.CharacterHasSkillSpecialty
        includeInJSON: false
    ,
        # Powers
        type: Backbone.HasMany
        key: 'powers'
        relatedModel: ORM.Characters.CharacterHasPower
        includeInJSON: false
    ,
        # Merits
        type: Backbone.HasMany
        key: 'merits'
        relatedModel: ORM.Characters.CharacterHasMerit
        includeInJSON: false
    ,
        # Flaws
        type: Backbone.HasMany
        key: 'flaws'
        relatedModel: ORM.Characters.CharacterHasFlaw
        includeInJSON: false
    ,
        # Derangements
        type: Backbone.HasMany
        key: 'derangements'
        relatedModel: ORM.Characters.CharacterHasDerangement
        includeInJSON: false
    ,
        # Combat Traits
        type: Backbone.HasMany
        key: 'combat_traits'
        relatedModel: ORM.Characters.CharacterHasCombatTrait
        includeInJSON: false
    ,
        # Miscellaneous Traits
        type: Backbone.HasMany
        key: 'misc_traits'
        relatedModel: ORM.Characters.CharacterHasMiscTrait
        includeInJSON: false
    ]

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        enabled      : raw.enabled
        user_id      : ORM.BaseModel.parse_int_field raw, 'user'
        # chronicle_id : Chronicle.Objects.Chronicle .get ORM.BaseModel.parse_int_field raw, 'chronicle'
        status       : Character.Status.get raw.status

        name             : raw.name
        creature_type_id : ORM.BaseModel.parse_int_field raw, 'creature_type_id'
        genealogy_id     : ORM.BaseModel.parse_int_field raw, 'genealogy_id'
        affiliation_id   : ORM.BaseModel.parse_int_field raw, 'affiliation_id'
        subgroup_id      : ORM.BaseModel.parse_int_field raw, 'subgroup_id'
        virtue_id        : ORM.BaseModel.parse_int_field raw, 'virtue_id'
        vice_id          : ORM.BaseModel.parse_int_field raw, 'vice_id'

        date_created     : ORM.BaseModel.parse_datetime_field raw, 'date_created'
        date_submitted   : ORM.BaseModel.parse_datetime_field raw, 'date_submitted'
        date_approved    : ORM.BaseModel.parse_datetime_field raw, 'date_approved'
        date_last_edited : ORM.BaseModel.parse_datetime_field raw, 'date_last_edited'

Models.Character.setup()
