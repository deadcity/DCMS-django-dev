###
  @file  character_power.coffee
  @brief Model specifying the specific power of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterPower extends ORM.characters.CharacterTrait
    @polymorphic_identity 'power'
