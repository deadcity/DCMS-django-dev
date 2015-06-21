###
  @file  skill.coffee
  @brief Model for character skills.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.SkillType extends ORM.traits.TraitType

ORM.traits.SkillType.reset()


class ORM.traits.Skill extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            skill_type_id : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'skill_type_id'

        return parsed

ORM.traits.Skill.reset()

ORM.polymorphic_identity 'skill', ORM.traits.Skill

ORM.traits.Skill.has().one 'skill_type',
    model: ORM.traits.SkillType
    inverse: 'skills'
