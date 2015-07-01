###
  @file  character_has_power.coffee
  @brief Model specifying the specific power of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasPower extends ORM.characters.CharacterHasTrait
    @polymorphic_identity 'power'
