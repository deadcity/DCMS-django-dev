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

    parse: (raw) ->
        return _.extend super,
            hide_from_player : raw.hide_from_player

ORM.traits.CharacterText.reset()

ORM.polymorphic_identity 'character_text', ORM.traits.CharacterText
