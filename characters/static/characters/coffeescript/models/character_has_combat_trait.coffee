###
  @file  character_has_combat_trait.coffee
  @brief Model specifying the specific combat-trait of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasCombatTrait extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasCombatTrait'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

        rating : undefined

    relations: [
        # Character
        type: Backbone.HasOne
        key: 'character'
        relatedModel: ORM.Character.Character
        includeInJSON: ORM.Character.Character.idAttribute
        autoFetch: true
        keySource: 'character_id'
        reverseRelationship:
            key: 'combat_traits'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.CombatTrait
        includeInJSON: ORM.Traits.CombatTrait.idAttribute
        autoFetch: true
        keySource: 'trait_id'
    ]

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

        rating : ORM.BaseModel.parse_int_field raw, 'rating'

Models.CharacterHasCombatTrait.setup()
