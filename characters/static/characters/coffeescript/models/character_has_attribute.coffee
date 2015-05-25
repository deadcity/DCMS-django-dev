###
  @file  character_has_attribute.coffee
  @brief Model specifying the specific attribute of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasAttribute extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasAttribute'

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
        id : ORM.BaseModel.parse_int_field raw, 'id'

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

        rating : ORM.BaseModel.parse_int_field raw, 'rating'

Models.CharacterHasAttribute.setup()
