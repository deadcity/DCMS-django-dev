###
  @file  character_has_flaw.coffee
  @brief Model specifying the specific flaw of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasFlaw extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            specification : undefined
            description   : undefined

    _parse: (raw) ->
        parsed = super

        ORM.parse parsed, raw, 'specification'
        ORM.parse parsed, raw, 'description'

        return parsed

ORM.characters.CharacterHasFlaw.reset()

ORM.polymorphic_identity 'flaw', ORM.characters.CharacterHasFlaw

ORM.characters.CharacterHasFlaw.has().one 'trait',
    model: ORM.traits.Flaw
    inverse: 'character_has_flaw'

ORM.characters.CharacterHasFlaw.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_flaws'

ORM.characters.Character.has().many 'character_flaws',
    collection: class CharacterHasFlaw_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasFlaw
    inverse: 'character'
