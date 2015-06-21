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

    # relations: [
    #     ORM.relation('user',      ORM.auth.User),
    #     ORM.relation('chronicle', ORM.chronicles.Chronicle),

    #     ORM.relation('creature_type', ORM.traits.CreatureType),
    #     ORM.relation('genealogy',     ORM.traits.Genealogy),
    #     ORM.relation('affiliation',   ORM.traits.Affiliation),
    #     ORM.relation('subgroup',      ORM.traits.Subgroup),

    #     ORM.relation_collection('attributes',        'characters.CharacterHasAttribute'),
    #     ORM.relation_collection('skills',            'characters.CharacterHasSkill'),
    #     ORM.relation_collection('skill_specialties', 'characters.CharacterHasSkillSpecialty'),
    #     ORM.relation_collection('powers',            'characters.CharacterHasPower'),
    #     ORM.relation_collection('merits',            'characters.CharacterHasMerit'),
    #     ORM.relation_collection('flaws',             'characters.CharacterHasFlaw'),
    #     ORM.relation_collection('combat_traits',     'characters.CharacterHasCombatTrait'),
    #     ORM.relation_collection('misc_traits',       'characters.CharacterHasMiscTrait'),
    # ]

    _parse: (raw) ->
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

ORM.characters.Character.reset()

ORM.characters.Character.has().one 'user',
    model: ORM.auth.User
    inverse: 'characters'

ORM.auth.User.has().many 'characters',
    collection: class Character_Collection extends Backbone.Collection
        model: ORM.characters.Character
    inverse: 'user'

ORM.characters.Character.has().one 'creature_type',
    model: ORM.traits.CreatureType
    inverse: 'character'

ORM.characters.Character.has().one 'genealogy',
    model: ORM.traits.Genealogy
    inverse: 'character'

ORM.characters.Character.has().one 'affiliation',
    model: ORM.traits.Affiliation
    inverse: 'character'

ORM.characters.Character.has().one 'subgroup',
    model: ORM.traits.Subgroup
    inverse: 'character'
