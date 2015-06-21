###
  @file  character_has_trait.coffee
  @brief Base model for "character-has-trait" models.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasTrait extends ORM.BaseModel
    @_polymorphic_on: 'trait_type'
    @_polymorphic_identity: {}

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/' + @constructor.name

    defaults: () ->
        id         : undefined
        trait_type : undefined

        character_id : undefined
        trait_id     : undefined

    _parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'
        ORM.parse     parsed, raw, 'trait_type'

        ORM.parse.int parsed, raw, 'character_id'
        ORM.parse.int parsed, raw, 'trait_id'

        return parsed

ORM.characters.CharacterHasTrait.reset()
