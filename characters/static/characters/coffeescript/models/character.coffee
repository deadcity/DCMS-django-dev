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
        DCMS.Settings.URL_PREFIX + '/rest/characters/Character'

    defaults: () ->
        id : undefined

        enabled      : true
        user_id      : undefined
        chronicle_id : undefined
        status       : Character.Status.EDITING

        name             : ''
        creature_type_id : undefined
        genealogy_id     : undefined
        affiliation_id   : undefined
        subgroup_id      : undefined

        date_created     : undefined
        date_submitted   : undefined
        date_approved    : undefined
        date_last_edited : undefined

    relations: [
        ORM.relation('user',      ORM.Auth.User),
        ORM.relation('chronicle', ORM.Chronicles.Chronicle),

        ORM.relation('creature_type', ORM.Traits.CreatureType),
        ORM.relation('genealogy',     ORM.Traits.Genealogy),
        ORM.relation('affiliation',   ORM.Traits.Affiliation),
        ORM.relation('subgroup',      ORM.Traits.Subgroup),

        ORM.relation_collection('attributes',        ORM.Characters.CharacterHasAttribute),
        ORM.relation_collection('skills',            ORM.Characters.CharacterHasSkill),
        ORM.relation_collection('skill_specialties', ORM.Characters.CharacterHasSkillSpecialty),
        ORM.relation_collection('powers',            ORM.Characters.CharacterHasPower),
        ORM.relation_collection('merits',            ORM.Characters.CharacterHasMerit),
        ORM.relation_collection('flaws',             ORM.Characters.CharacterHasFlaw),
        ORM.relation_collection('combat_traits',     ORM.Characters.CharacterHasCombatTrait),
        ORM.relation_collection('misc_traits',       ORM.Characters.CharacterHasMiscTrait),
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

        date_created     : ORM.BaseModel.parse_datetime_field raw, 'date_created'
        date_submitted   : ORM.BaseModel.parse_datetime_field raw, 'date_submitted'
        date_approved    : ORM.BaseModel.parse_datetime_field raw, 'date_approved'
        date_last_edited : ORM.BaseModel.parse_datetime_field raw, 'date_last_edited'

Models.Character.setup()
