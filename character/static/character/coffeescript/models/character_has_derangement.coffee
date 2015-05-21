###
  @file  character_has_derangement.coffee
  @brief Model specifying the specific derangement of a specific character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.CharacterHasDerangement extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasDerangement'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

        specification : undefined
        description   : undefined

    relations: [
        # Character
        type: Backbone.HasOne
        key: 'character'
        relatedModel: ORM.Character.Character
        includeInJSON: ORM.Character.Character.idAttribute
        autoFetch: true
        keySource: 'character_id'
        reverseRelationship:
            key: 'derangements'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.Derangement
        includeInJSON: ORM.Traits.Derangement.idAttribute
        autoFetch: true
        keySource: 'trait_id'
    ]

    parse: (raw) ->
        attr =
            id : parseInt raw.id, 10

            character_id : parseInt raw.character_id, 10
            trait_id     : parseInt raw.trait_id,     10

            specification : raw.specification
            description   : raw.description

        attr.id = null if _.isNaN attr.id

        attr.character_id = null if _.isNaN attr.character_id
        attr.trait_id     = null if _.isNaN attr.trait_id

        return attr

Models.CharacterHasDerangement.setup()
