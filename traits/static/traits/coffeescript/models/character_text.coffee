###
  @file  character_text.coffee
  @brief Model for character texts.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.CharacterText extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            hide_from_player : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'hide_from_player'

        return parsed

ORM.traits.CharacterText.reset()

ORM.polymorphic_identity 'character_text', ORM.traits.CharacterText
