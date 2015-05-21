###
  @file  character_has_combat_trait.coffee
  @brief Model specifying the specific combat-trait of a specific character.
###


Models = Tools.create_namespace 'Character.Models'


class Models.CharacterHasCombatTrait extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasCombatTrait'

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
        attr =
            id : parseInt raw.id, 10

            character_id : parseInt raw.character_id, 10
            trait_id     : parseInt raw.trait_id,     10

            rating : parseInt raw.rating, 10

        attr.id = null if _.isNaN attr.id

        attr.character_id = null if _.isNaN attr.character_id
        attr.trait_id     = null if _.isNaN attr.trait_id

        attr.rating = null if _.isNaN attr.rating

        return attr

Models.CharacterHasCombatTrait.setup()
