###
  @file  character_has_character_text.coffee
  @brief Model specifying the specific text of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasCharacterText extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            text : undefined

    parse: (raw) ->
        return _.extend super,
            text : raw.text

ORM.characters.CharacterHasCharacterText.reset()

ORM.polymorphic_identity 'character_text', ORM.characters.CharacterHasCharacterText

ORM.characters.CharacterHasCharacterText.has().one 'trait',
    model: ORM.traits.CharacterText
    inverse: 'character_has_character_text'

ORM.characters.CharacterHasCharacterText.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_texts'

ORM.characters.Character.has().many 'character_texts',
    collection: class CharacterHasCharacterText_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasCharacterText
    inverse: 'character'
