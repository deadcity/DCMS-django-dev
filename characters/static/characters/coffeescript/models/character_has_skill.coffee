###
  @file  character_has_skill.coffee
  @brief Model specifying the specific skill of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasSkill extends ORM.characters.CharacterHasTrait
    @polymorphic_identity 'skill'

    defaults: () ->
        return _.extend super,
            rating : 0

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed
