###
  @file  character_has_misc_trait.coffee
  @brief Model specifying the specific miscellaneous trait of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasMiscTrait extends ORM.characters.CharacterHasTrait
    @polymorphic_identity 'misc_trait'

    defaults: () ->
        return _.extend super,
            rating      : undefined
            description : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'
        ORM.parse     parsed, raw, 'description'

        return parsed
