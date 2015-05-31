###
  @file  trait.coffee
  @brief Base models for traits and trait-types.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.TraitType extends ORM.BaseModel
    defaults: () ->
        id : undefined

        name  : undefined
        label : ''

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        name  : raw.name
        label : raw.label

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
        DCMS.Settings.URL_PREFIX + '/traits/Trait'

    defaults: () ->
        id             : undefined
        _discriminator : undefined

        name  : undefined
        label : ''

    parse: (raw) ->
        id             : ORM.BaseModel.parse_int_field raw, 'id'
        _discriminator : raw._discriminator

        name  : raw.name
        label : raw.label

Models.Trait.setup()
