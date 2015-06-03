###
  @file  skill.coffee
  @brief Model for character skills.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.SkillType extends Models.TraitType
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/SkillType'

Models.SkillType.setup()


class Models.Skill extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Skill'

    defaults: () ->
        return _.extend super,
            skill_type_id : undefined

    relations: [ORM.relation 'skill_type', Models.SkillType]

    parse: (raw) ->
        return _.extend super,
            skill_type_id : ORM.BaseModel.parse_int_field raw, 'skill_type_id'

Models.Skill.setup()
