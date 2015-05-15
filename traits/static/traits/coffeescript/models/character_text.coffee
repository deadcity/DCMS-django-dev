###
  @file  character_text.coffee
  @brief Model for character texts.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.CharacterText extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/CharacterText"

    defaults: () ->
        _.extends super,
            hide_from_player : undefined

    parse: (raw) ->
        attr = super

        attr.hide_from_player = raw.hide_from_player

        return attr

Models.CharacterText.setup()
