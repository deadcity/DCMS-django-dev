###
  @file  character_merit.coffee
  @brief Model specifying the specific merit of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterMerit extends ORM.characters.CharacterTrait
    @polymorphic_identity 'merit'

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
