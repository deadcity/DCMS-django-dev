from common.generators import Serializer_Metaclass
import traits


class AttributeTypeSerializer   : __metaclass__ = Serializer_Metaclass(traits.models.AttributeType)
class DerangementTypeSerializer : __metaclass__ = Serializer_Metaclass(traits.models.DerangementType)
class FlawTypeSerializer        : __metaclass__ = Serializer_Metaclass(traits.models.FlawType)
class MeritTypeSerializer       : __metaclass__ = Serializer_Metaclass(traits.models.MeritType)
class SkillTypeSerializer       : __metaclass__ = Serializer_Metaclass(traits.models.SkillType)
class ViceSerializer            : __metaclass__ = Serializer_Metaclass(traits.models.Vice)
class VirtueSerializer          : __metaclass__ = Serializer_Metaclass(traits.models.Virtue)

class AffiliationSerializer   : __metaclass__ = Serializer_Metaclass(traits.models.Affiliation)
class AttributeSerializer     : __metaclass__ = Serializer_Metaclass(traits.models.Attribute)
class CharacterTextSerializer : __metaclass__ = Serializer_Metaclass(traits.models.CharacterText)
class CombatTraitSerializer   : __metaclass__ = Serializer_Metaclass(traits.models.CombatTrait)
class CreatureTypeSerializer  : __metaclass__ = Serializer_Metaclass(traits.models.CreatureType)
class DerangementSerializer   : __metaclass__ = Serializer_Metaclass(traits.models.Derangement)
class FlawSerializer          : __metaclass__ = Serializer_Metaclass(traits.models.Flaw)
class GenealogySerializer     : __metaclass__ = Serializer_Metaclass(traits.models.Genealogy)
class MeritSerializer         : __metaclass__ = Serializer_Metaclass(traits.models.Merit)
class MiscTraitSerializer     : __metaclass__ = Serializer_Metaclass(traits.models.MiscTrait)
class PowerSerializer         : __metaclass__ = Serializer_Metaclass(traits.models.Power)
class SkillSerializer         : __metaclass__ = Serializer_Metaclass(traits.models.Skill)
class SubgroupSerializer      : __metaclass__ = Serializer_Metaclass(traits.models.Subgroup)
