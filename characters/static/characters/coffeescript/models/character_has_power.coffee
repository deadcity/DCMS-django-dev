###
  @file  character_has_power.coffee
  @brief Model specifying the specific power of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasPower extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasPower'

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
        id : ORM.BaseModel.parse_int_field raw, 'id'

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

Models.CharacterHasPower.setup()
