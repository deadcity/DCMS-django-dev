###
  @file  character_has_trait.coffee
  @brief Base model for "character-has-trait" models.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasTrait extends ORM.BaseModel
    @_polymorphic_on: '_discriminator'
    @_polymorphic_identity: {}

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/characters/' + @constructor.name

    defaults: () ->
        id             : undefined
        _discriminator : undefined

        character_id : undefined
        trait_id     : undefined

    parse: (raw) ->
        id             : ORM.parse.int raw, 'id'
        _discriminator : raw._discriminator

        character_id : ORM.parse.int raw, 'character_id'
        trait_id     : ORM.parse.int raw, 'trait_id'

ORM.characters.CharacterHasTrait.reset()
