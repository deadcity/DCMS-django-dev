###
  @file  character_has_misc_trait.coffee
  @brief Model specifying the specific miscellaneous trait of a specific character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.CharacterHasMiscTrait extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasMiscTrait'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

        rating      : undefined
        description : undefined

    relations: [
        # Character
        type: Backbone.HasOne
        key: 'character'
        relatedModel: ORM.Character.Character
        includeInJSON: ORM.Character.Character.idAttribute
        autoFetch: true
        keySource: 'character_id'
        reverseRelationship:
            key: 'misc_traits'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.MiscTrait
        includeInJSON: ORM.Traits.MiscTrait.idAttribute
        autoFetch: true
        keySource: 'trait_id'
    ]

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

        rating      : ORM.BaseModel.parse_int_field raw, 'rating'
        description : raw.description

Models.CharacterHasMiscTrait.setup()
