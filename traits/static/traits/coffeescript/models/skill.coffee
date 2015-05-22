###
  @file  skill.coffee
  @brief Model for character skills.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.SkillType extends Models.TraitType
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/SkillType'

Models.SkillType.setup()


class Models.Skill extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/Skill'

    defaults: () ->
        return _.extend super,
            skill_type_id : undefined

    relations: [
        type: Backbone.HasOne
        key: 'skill_type'
        relatedModel: Models.SkillType
        includeInJSON: Models.SkillType.idAttribute
        autoFetch: true
        keySource: 'skill_type_id'
    ]

    parse: (raw) ->
        return _.extend super,
            skill_type_id : ORM.BaseModel.parse_int_field raw, 'skill_type_id'

Models.Skill.setup()
