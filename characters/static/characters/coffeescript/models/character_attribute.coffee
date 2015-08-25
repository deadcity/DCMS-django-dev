###
  @file  character_attribute.coffee
  @brief Model specifying the specific attribute of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterAttribute extends ORM.characters.CharacterTrait
    @polymorphic_identity 'attribute'

    defaults: () ->
        return _.extend super,
            rating : 1

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'rating'

        return parsed
