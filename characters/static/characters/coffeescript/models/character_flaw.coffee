###
  @file  character_flaw.coffee
  @brief Model specifying the specific flaw of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterFlaw extends ORM.characters.CharacterTrait
    @polymorphic_identity 'flaw'

    defaults: () ->
        return _.extend super,
            rating        : undefined
            specification : undefined
            description   : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'
        ORM.parse     parsed, raw, 'specification'
        ORM.parse     parsed, raw, 'description'

        return parsed
