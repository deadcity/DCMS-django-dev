###
  @file  trait.coffee
  @brief Base models for traits and trait-types.
###


Models = Tools.create_namespace 'ORM.traits'


class Models.TraitType extends ORM.BaseModel
    defaults: () ->
        id : undefined

        chronicle_id : undefined
        name         : undefined
        label        : ''

    relations: [ORM.relation 'chronicle', ORM.chronicles.ChronicleBase]

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        chronicle_id : ORM.BaseModel.parse_int_field raw, 'id'
        name         : raw.name
        label        : raw.label

Models.TraitType.setup()


class Models.Trait extends ORM.BaseModel
    subModelTypeAttribute: '_discriminator'
    subModelTypes:
        'affiliation'    : 'Affiliation'
        'attribute'      : 'Attribute'
        'character_text' : 'CharacterText'
        'combat_trait'   : 'CombatTrait'
        'creature_type'  : 'CreatureType'
        'flaw'           : 'Flaw'
        'genealogy'      : 'Genealogy'
        'merit'          : 'Merit'
        'misc_trait'     : 'MiscTrait'
        'power'          : 'Power'
        'power_group'    : 'PowerGroup'
        'skill'          : 'Skill'
        'subgroup'       : 'Subgroup'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Trait'

    defaults: () ->
        id             : undefined
        _discriminator : undefined

        chronicle_id : undefined
        name         : undefined
        label        : ''

    relations: [ORM.relation 'chronicle', ORM.chronicles.ChronicleBase]

    parse: (raw) ->
        id             : ORM.BaseModel.parse_int_field raw, 'id'
        _discriminator : raw._discriminator

        chronicle_id : ORM.BaseModel.parse_int_field raw, 'id'
        name         : raw.name
        label        : raw.label

Models.Trait.setup()
