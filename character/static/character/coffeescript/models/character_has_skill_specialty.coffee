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
        attr =
            id : parseInt raw.id, 10

            character_id : parseInt raw.character_id, 10
            trait_id     : parseInt raw.trait_id,     10

            specialty : raw.specialty

        attr.id = null if _.isNaN attr.id

        attr.character_id = null if _.isNaN attr.character_id
        attr.trait_id     = null if _.isNaN attr.trait_id

        return attr

Models.CharacterHasSkillSpecialty.setup()
