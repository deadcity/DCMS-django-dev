###
  @file  character_has_text.coffee
  @brief Model specifying the specific text of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasText extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasText'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

        text : undefined

    relations: [
        # Character
        type: Backbone.HasOne
        key: 'character'
        relatedModel: ORM.Character.Character
        includeInJSON: ORM.Character.Character.idAttribute
        autoFetch: true
        keySource: 'character_id'
        reverseRelationship:
            key: 'skill_specialties'
    ,
        # Trait
        type: Backbone.HasOne
        key: 'trait'
        relatedModel: ORM.Traits.Skill
        includeInJSON: ORM.Traits.Skill.idAttribute
        autoFetch: true
        keySource: 'trait_id'
    ]

    parse: (raw) ->
        id : ORM.BaseModel.parse_int_field raw, 'id'

        character_id : ORM.BaseModel.parse_int_field raw, 'character_id'
        trait_id     : ORM.BaseModel.parse_int_field raw, 'trait_id'

        text : raw.text

Models.CharacterHasText.setup()
