###
  @file  character_has_skill_specialty.coffee
  @brief Model specifying the specific skill specialty of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasSkillSpecialty extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            specialty : undefined

    parse: (raw) ->
        return _.extend super,
            specialty : raw.specialty

ORM.characters.CharacterHasSkillSpecialty.reset()

ORM.polymorphic_identity 'skill_specialty', ORM.characters.CharacterHasSkillSpecialty

ORM.characters.CharacterHasSkillSpecialty.has().one 'trait',
    model: ORM.traits.Skill
    inverse: 'character_has_skill_specialties'

ORM.characters.CharacterHasSkillSpecialty.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_skill_specialties'

ORM.characters.Character.has().many 'character_skill_specialties',
    collection: class CharacterHasSkillSpecialty_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasSkillSpecialty
    inverse: 'character'
