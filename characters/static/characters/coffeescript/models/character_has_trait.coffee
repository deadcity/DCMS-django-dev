###
  @file  character_has_trait.coffee
  @brief Base model for "character-has-trait" models.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasTrait extends ORM.BaseModel
    @polymorphic_on 'trait_type'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/' + @constructor.name

    defaults: () ->
        id         : undefined
        trait_type : undefined

        character_id : undefined
        trait_id     : undefined

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'
        ORM.parse     parsed, raw, 'trait_type'

        ORM.parse.int parsed, raw, 'character_id'
        ORM.parse.int parsed, raw, 'trait_id'

        return parsed

    @has_one 'character', Model : 'ORM.characters.Character'
    @has_one 'trait',     Model : 'ORM.traits.Trait'
