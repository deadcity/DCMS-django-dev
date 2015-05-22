###
  @file  character_has_merit.coffee
  @brief Model specifying the specific merit of a specific character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.CharacterHasMerit extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasMerit'

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
            key: 'merits'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.Merit
        includeInJSON: ORM.Traits.Merit.idAttribute
        autoFetch: true
        keySource: 'trait_id'
    ]

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

        specification : raw.specification
        description   : raw.description

Models.CharacterHasMerit.setup()
