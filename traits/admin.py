from django.contrib import admin

from common.generators import EnumAdmin_Metaclass, TraitAdmin_Metaclass
import traits.models as models


class AttributeTypeAdmin   : __metaclass__ = EnumAdmin_Metaclass(models.AttributeType)
class DerangementTypeAdmin : __metaclass__ = EnumAdmin_Metaclass(models.DerangementType)
class FlawTypeAdmin        : __metaclass__ = EnumAdmin_Metaclass(models.FlawType)
class MeritTypeAdmin       : __metaclass__ = EnumAdmin_Metaclass(models.MeritType)
class SkillTypeAdmin       : __metaclass__ = EnumAdmin_Metaclass(models.SkillType)
class ViceAdmin            : __metaclass__ = EnumAdmin_Metaclass(models.Vice)
class VirtueAdmin          : __metaclass__ = EnumAdmin_Metaclass(models.Virtue)

admin.site.register(models.AttributeType,   AttributeTypeAdmin)
admin.site.register(models.DerangementType, DerangementTypeAdmin)
admin.site.register(models.FlawType,        FlawTypeAdmin)
admin.site.register(models.MeritType,       MeritTypeAdmin)
admin.site.register(models.SkillType,       SkillTypeAdmin)
admin.site.register(models.Vice,            ViceAdmin)
admin.site.register(models.Virtue,          VirtueAdmin)

class AffiliationAdmin   : __metaclass__ = TraitAdmin_Metaclass(models.Affiliation)
class AttributeAdmin     : __metaclass__ = TraitAdmin_Metaclass(models.Attribute)
class CharacterTextAdmin : __metaclass__ = TraitAdmin_Metaclass(models.CharacterText)
class CombatTraitAdmin   : __metaclass__ = TraitAdmin_Metaclass(models.CombatTrait)
class CreatureTypeAdmin  : __metaclass__ = TraitAdmin_Metaclass(models.CreatureType)
class DerangementAdmin   : __metaclass__ = TraitAdmin_Metaclass(models.Derangement)
class FlawAdmin          : __metaclass__ = TraitAdmin_Metaclass(models.Flaw)
class GenealogyAdmin     : __metaclass__ = TraitAdmin_Metaclass(models.Genealogy)
class MeritAdmin         : __metaclass__ = TraitAdmin_Metaclass(models.Merit)
class MiscTraitAdmin     : __metaclass__ = TraitAdmin_Metaclass(models.MiscTrait)
class PowerAdmin         : __metaclass__ = TraitAdmin_Metaclass(models.Power)
class SkillAdmin         : __metaclass__ = TraitAdmin_Metaclass(models.Skill)
class SubgroupAdmin      : __metaclass__ = TraitAdmin_Metaclass(models.Subgroup)

admin.site.register(models.Affiliation,   AffiliationAdmin)
admin.site.register(models.Attribute,     AttributeAdmin)
admin.site.register(models.CharacterText, CharacterTextAdmin)
admin.site.register(models.CombatTrait,   CombatTraitAdmin)
admin.site.register(models.CreatureType,  CreatureTypeAdmin)
admin.site.register(models.Derangement,   DerangementAdmin)
admin.site.register(models.Flaw,          FlawAdmin)
admin.site.register(models.Genealogy,     GenealogyAdmin)
admin.site.register(models.Merit,         MeritAdmin)
admin.site.register(models.MiscTrait,     MiscTraitAdmin)
admin.site.register(models.Power,         PowerAdmin)
admin.site.register(models.Skill,         SkillAdmin)
admin.site.register(models.Subgroup,      SubgroupAdmin)
