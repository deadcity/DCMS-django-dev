###
  @file  character_has_attribute.coffee
  @brief Model specifying the specific attribute of a specific character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.CharacterHasAttribute extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasAttribute'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

        rating : 1

    relations: [
        # Character
        type: Backbone.HasOne
        key: 'character'
        relatedModel: ORM.Character.Character
        includeInJSON: ORM.Character.Character.idAttribute
        autoFetch: true
        keySource: 'character_id'
        reverseRelationship:
            key: 'attributes'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.Attribute
        includeInJSON: ORM.Traits.Attribute.idAttribute
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

Models.CharacterHasAttribute.setup()
