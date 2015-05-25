###
  @file  character_has_skill.coffee
  @brief Model specifying the specific skill of a specific character.
###


Models = Tools.create_namespace 'ORM.Characters'


class Models.CharacterHasSkill extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/characters/CharacterHasSkill'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

        rating : 0

    relations: [
        # Character
        type: Backbone.HasOne
        key: 'character'
        relatedModel: ORM.Character.Character
        includeInJSON: ORM.Character.Character.idAttribute
        autoFetch: true
        keySource: 'character_id'
        reverseRelationship:
            key: 'skills'
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

        rating : ORM.BaseModel.parse_int_field raw, 'rating'

Models.CharacterHasSkill.setup()
