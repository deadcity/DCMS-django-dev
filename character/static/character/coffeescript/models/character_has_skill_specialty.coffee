###
  @file  character_has_skill_specialty.coffee
  @brief Model specifying the specific skill specialty of a specific character.
###


Models = Tools.create_namespace 'ORM.Character'


class Models.CharacterHasSkillSpecialty extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/character/CharacterHasSkillSpecialty'

    defaults: () ->
        id : undefined

        character_id : undefined
        trait_id     : undefined

        specialty : undefined

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

        specialty : raw.specialty

Models.CharacterHasSkillSpecialty.setup()
