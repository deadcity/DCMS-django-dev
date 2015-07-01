###
  @file  skill.coffee
  @brief Model for character skills.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.SkillType extends ORM.traits.TraitType


class ORM.traits.Skill extends ORM.traits.Trait
    @polymorphic_identity 'skill'

    defaults: () ->
        return _.extend super,
            skill_type_id : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'skill_type_id'

        return parsed

    @has_one 'skill_type',
        Model : ORM.traits.SkillType
