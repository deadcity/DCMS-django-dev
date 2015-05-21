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
        attr =
            id : parseInt raw.id, 10

            character_id : parseInt raw.character_id, 10
            trait_id     : parseInt raw.trait_id,     10

            rating      : parseInt raw.rating, 10
            description : raw.description

        attr.id = null if _.isNaN attr.id

        attr.character_id = null if _.isNaN attr.character_id
        attr.trait_id     = null if _.isNaN attr.trait_id

        attr.rating = null if _.isNaN attr.rating

        return attr

Models.CharacterHasMiscTrait.setup()
