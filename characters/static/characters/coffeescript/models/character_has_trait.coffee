###
  @file  character_has_trait.coffee
  @brief Base model for "character-has-trait" models.
###


Models = Tools.create_namespace 'ORM.characters'


class Models.CharacterHasTrait extends ORM.BaseModel
    subModelTypeAttribute: '_discriminator'
    subModelTypes:
        'attribute'       : 'CharacterHasAttribute'
        'character_text'  : 'CharacterHasCharacterText'
        'combat_trait'    : 'CharacterHasCombatTrait'
        'flaw'            : 'CharacterHasFlaw'
        'merit'           : 'CharacterHasMerit'
        'misc_trait'      : 'CharacterHasMiscTrait'
        'power'           : 'CharacterHasPower'
        'skill'           : 'CharacterHasSkill'
        'skill_specialty' : 'CharacterHasSkillSpecialty'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/CharacterHasTrait'

    defaults: () ->
        id             : undefined
        _discriminator : undefined

        character_id : undefined
        trait_id     : undefined

    relations: [
        ORM.relation('character', ORM.characters.Character),
        ORM.relation('trait',     ORM.traits.Trait),
    ]

    parse: (raw) ->
        id             : ORM.BaseModel.parse_int_field raw, 'id'
        _discriminator : raw._discriminator

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

Models.CharacterHasTrait.setup()
