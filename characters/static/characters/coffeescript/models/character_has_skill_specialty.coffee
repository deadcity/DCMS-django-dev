###
  @file  character_has_skill_specialty.coffee
  @brief Model specifying the specific skill specialty of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasSkillSpecialty extends ORM.characters.CharacterHasTrait
    @polymorphic_identity 'skill_specialty'

    defaults: () ->
        return _.extend super,
            specialty : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'specialty'

        return parsed
