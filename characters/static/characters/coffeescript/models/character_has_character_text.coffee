###
  @file  character_has_character_text.coffee
  @brief Model specifying the specific text of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasCharacterText extends ORM.characters.CharacterHasTrait
    @polymorphic_identity 'character_text'

    defaults: () ->
        return _.extend super,
            text : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'text'

        return parsed
