###
  @file  character_has_attribute.coffee
  @brief Model specifying the specific attribute of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasAttribute extends ORM.characters.CharacterHasTrait
    @polymorphic_identity 'attribute'

    defaults: () ->
        return _.extend super,
            rating : 1

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed
