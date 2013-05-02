from common.generators import Serializer_Metaclass
import character


class CharacterSerializer : __metaclass__ = Serializer_Metaclass(character.models.Character)

class CharacterHasAttribute      : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasAttribute)
class CharacterHasCombatTrait    : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasCombatTrait)
class CharacterHasDerangement    : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasDerangement)
class CharacterHasFlaw           : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasFlaw)
class CharacterHasMerit          : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasMerit)
class CharacterHasMiscTrait      : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasMiscTrait)
class CharacterHasPower          : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasPower)
class CharacterHasSkill          : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasSkill)
class CharacterHasSkillSpecialty : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasSkillSpecialty)
class CharacterHasText           : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasText)
class CharacterHasTrait          : __metaclass__ = Serializer_Metaclass(character.models.CharacterHasTrait)
