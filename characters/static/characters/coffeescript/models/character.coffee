###
  @file  character.coffee
  @brief Model for character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.Character extends ORM.BaseModel
    @Status: Tools.enum 'Status', [
        'EDITING'
        'SUBMITTED'
        'APPROVED'
        'ACTIVE'
        'DECEASED'
        'INACTIVE'
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

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'

        ORM.parse      parsed, raw, 'enabled'
        ORM.parse.int  parsed, raw, 'user_id'
        ORM.parse.int  parsed, raw, 'chronicle_id'
        ORM.parse.enum parsed, raw, 'status', Character.Status

        ORM.parse     parsed, raw, 'name'
        ORM.parse.int parsed, raw, 'creature_type_id'
        ORM.parse.int parsed, raw, 'genealogy_id'
        ORM.parse.int parsed, raw, 'affiliation_id'
        ORM.parse.int parsed, raw, 'subgroup_id'

        ORM.parse.datetime parsed, raw, 'date_created'
        ORM.parse.datetime parsed, raw, 'date_submitted'
        ORM.parse.datetime parsed, raw, 'date_approved'
        ORM.parse.datetime parsed, raw, 'date_last_edited'

        return parsed

    @has_one 'user',      Model : 'ORM.auth.User'
    @has_one 'chronicle', Model : 'ORM.chronicles.Chronicle'

    @has_one 'creature_type', Model : 'ORM.traits.CreatureType'
    @has_one 'genealogy',     Model : 'ORM.traits.Genealogy'
    @has_one 'affiliation',   Model : 'ORM.traits.Affiliation'
    @has_one 'subgroup',      Model : 'ORM.traits.Subgroup'

    @has_many 'character_attributes',
        Model     : 'ORM.characters.CharacterAttribute'
        attribute : 'character_id'

    @has_many 'character_skills',
        Model     : 'ORM.characters.CharacterSkill'
        attribute : 'character_id'

    @has_many 'character_skill_specialties',
        Model     : 'ORM.characters.CharacterSkillSpecialty',
        attribute : 'character_id'

    @has_many 'character_powers',
        Model     : 'ORM.characters.CharacterPower',
        attribute : 'character_id'

    @has_many 'character_merits',
        Model     : 'ORM.characters.CharacterMerit',
        attribute : 'character_id'

    @has_many 'character_flaws',
        Model     : 'ORM.characters.CharacterFlaw',
        attribute : 'character_id'

    @has_many 'character_combat_traits',
        Model     : 'ORM.characters.CharacterCombatTrait',
        attribute : 'character_id'

    @has_many 'character_misc_traits',
        Model     : 'ORM.characters.CharacterMiscTrait',
        attribute : 'character_id'
