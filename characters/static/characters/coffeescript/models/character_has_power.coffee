###
  @file  character_has_power.coffee
  @brief Model specifying the specific power of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasPower extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

ORM.characters.CharacterHasPower.reset()

ORM.polymorphic_identity 'power', ORM.characters.CharacterHasPower

ORM.characters.CharacterHasPower.has().one 'trait',
    model: ORM.traits.Power
    inverse: 'character_has_power'

ORM.characters.CharacterHasPower.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_powers'

ORM.characters.Character.has().many 'character_powers',
    collection: class CharacterHasPower_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasPower
    inverse: 'character'
