###
  @file  character_has_power.coffee
  @brief Model specifying the specific power of a specific character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.CharacterHasPower extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasPower'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

    relations: [
        # Character
        type: Backbone.HasOne
        key: 'character'
        relatedModel: ORM.Character.Character
        includeInJSON: ORM.Character.Character.idAttribute
        autoFetch: true
        keySource: 'character_id'
        reverseRelationship:
            key: 'powers'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.Power
        includeInJSON: ORM.Traits.Power.idAttribute
        autoFetch: true
        keySource: 'trait_id'
    ]

    parse: (raw) ->
        attr =
            id : parseInt raw.id, 10

            character_id : parseInt raw.character_id, 10
            trait_id     : parseInt raw.trait_id,     10

        attr.id = null if _.isNaN attr.id

        attr.character_id = null if _.isNaN attr.character_id
        attr.trait_id     = null if _.isNaN attr.trait_id

        return attr

Models.CharacterHasPower.setup()
