###
  @file  character.coffee
  @brief Model for character.
###


Models = Tools.create_namespace 'ORM.characters'


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
        ORM.relation('user',      ORM.auth.User),
        ORM.relation('chronicle', ORM.chronicles.Chronicle),

        ORM.relation('creature_type', ORM.traits.CreatureType),
        ORM.relation('genealogy',     ORM.traits.Genealogy),
        ORM.relation('affiliation',   ORM.traits.Affiliation),
        ORM.relation('subgroup',      ORM.traits.Subgroup),

        ORM.relation_collection('attributes',        'characters.CharacterHasAttribute'),
        ORM.relation_collection('skills',            'characters.CharacterHasSkill'),
        ORM.relation_collection('skill_specialties', 'characters.CharacterHasSkillSpecialty'),
        ORM.relation_collection('powers',            'characters.CharacterHasPower'),
        ORM.relation_collection('merits',            'characters.CharacterHasMerit'),
        ORM.relation_collection('flaws',             'characters.CharacterHasFlaw'),
        ORM.relation_collection('combat_traits',     'characters.CharacterHasCombatTrait'),
        ORM.relation_collection('misc_traits',       'characters.CharacterHasMiscTrait'),
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
