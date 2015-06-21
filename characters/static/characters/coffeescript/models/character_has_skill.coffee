###
  @file  character_has_skill.coffee
  @brief Model specifying the specific skill of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasSkill extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            rating : 0

    _parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed

ORM.characters.CharacterHasSkill.reset()

ORM.polymorphic_identity 'skill', ORM.characters.CharacterHasSkill

ORM.characters.CharacterHasSkill.has().one 'trait',
    model: ORM.traits.Skill
    inverse: 'character_has_skill'

ORM.characters.CharacterHasSkill.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_skills'

ORM.characters.Character.has().many 'character_skills',
    collection: class CharacterHasSkill_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasSkill
    inverse: 'character'
