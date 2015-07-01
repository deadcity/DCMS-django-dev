###
  @file  character_text.coffee
  @brief Model for character texts.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.CharacterText extends ORM.traits.Trait
    @polymorphic_identity 'character_text'

    defaults: () ->
        return _.extend super,
            hide_from_player : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'hide_from_player'

        return parsed
