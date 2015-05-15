###
  @file  trait.coffee
  @brief Base models for traits and trait-types.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.TraitType extends ORM.BaseModel
    defaults: () ->
        id   : undefined
        name : undefined

    parse: (raw) ->
        attr =
            id   : parseInt raw.id, 10
            name : raw.name

        attr.id = null if _.isNaN attr.id

        return attr

Models.TraitType.setup()


class Models.Trait extends ORM.BaseModel
    subModelTypeAttribute: '_discriminator'
    subModelTypes:
        'affiliation'    : 'Affiliation'
        'attribute'      : 'Attribute'
        'character_text' : 'CharacterText'
        'combat_trait'   : 'CombatTrait'
        'creature_type'  : 'CreatureType'
        'derangement'    : 'Derangement'
        'flaw'           : 'Flaw'
        'genealogy'      : 'Genealogy'
        'merit'          : 'Merit'
        'misc_trait'     : 'MiscTrait'
        'power_group'    : 'PowerGroup'
        'skill'          : 'Skill'
        'subgroup'       : 'Subgroup'

    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Trait"

    defaults: () ->
        id             : undefined
        _discriminator : undefined
        enabled        : undefined
        name           : undefined

    parse: (raw) ->
        attr =
            id             : parseInt raw.id, 10
            _discriminator : raw._discriminator
            enabled        : raw.enabled
            name           : raw.name

        attr.id = null if _.isNaN attr.id

        return attr

Models.Trait.setup()
