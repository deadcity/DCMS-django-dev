###
  @file  character_has_flaw.coffee
  @brief Model specifying the specific flaw of a specific character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.CharacterHasFlaw extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasFlaw'

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
            key: 'flaws'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.Flaw
        includeInJSON: ORM.Traits.Flaw.idAttribute
        autoFetch: true
        keySource: 'trait_id'
    ]

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

        specification : raw.specification
        description   : raw.description

Models.CharacterHasFlaw.setup()
