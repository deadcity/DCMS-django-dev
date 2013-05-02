from django.db.models.loading import get_model
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer

from common.generators import APIDetail_Metaclass, APIList_Metaclass
import traits.models as models
import traits.serializers as serializers


# # # # # # #
# API Views #
# # # # # # #

# Detail Views

class AttributeTypeDetail   : __metaclass__ = APIDetail_Metaclass(models.AttributeType,   serializers.AttributeTypeSerializer)
class DerangementTypeDetail : __metaclass__ = APIDetail_Metaclass(models.DerangementType, serializers.DerangementTypeSerializer)
class FlawTypeDetail        : __metaclass__ = APIDetail_Metaclass(models.FlawType,        serializers.FlawTypeSerializer)
class MeritTypeDetail       : __metaclass__ = APIDetail_Metaclass(models.MeritType,       serializers.MeritTypeSerializer)
class SkillTypeDetail       : __metaclass__ = APIDetail_Metaclass(models.SkillType,       serializers.SkillTypeSerializer)

class AffiliationDetail   : __metaclass__ = APIDetail_Metaclass(models.Affiliation,   serializers.AffiliationSerializer)
class AttributeDetail     : __metaclass__ = APIDetail_Metaclass(models.Attribute,     serializers.AttributeSerializer)
class CharacterTextDetail : __metaclass__ = APIDetail_Metaclass(models.CharacterText, serializers.CharacterTextSerializer)
class CombatTraitDetail   : __metaclass__ = APIDetail_Metaclass(models.CombatTrait,   serializers.CombatTraitSerializer)
class CreatureTypeDetail  : __metaclass__ = APIDetail_Metaclass(models.CreatureType,  serializers.CreatureTypeSerializer)
class DerangementDetail   : __metaclass__ = APIDetail_Metaclass(models.Derangement,   serializers.DerangementSerializer)
class FlawDetail          : __metaclass__ = APIDetail_Metaclass(models.Flaw,          serializers.FlawSerializer)
class GenealogyDetail     : __metaclass__ = APIDetail_Metaclass(models.Genealogy,     serializers.GenealogySerializer)
class MeritDetail         : __metaclass__ = APIDetail_Metaclass(models.Merit,         serializers.MeritSerializer)
class MiscTraitDetail     : __metaclass__ = APIDetail_Metaclass(models.MiscTrait,     serializers.MiscTraitSerializer)
class PowerDetail         : __metaclass__ = APIDetail_Metaclass(models.Power,         serializers.PowerSerializer)
class SkillDetail         : __metaclass__ = APIDetail_Metaclass(models.Skill,         serializers.SkillSerializer)
class SubgroupDetail      : __metaclass__ = APIDetail_Metaclass(models.Subgroup,      serializers.SubgroupSerializer)
class ViceDetail          : __metaclass__ = APIDetail_Metaclass(models.Vice,          serializers.ViceSerializer)
class VirtueDetail        : __metaclass__ = APIDetail_Metaclass(models.Virtue,        serializers.VirtueSerializer)

# List Views

class AttributeTypeList   : __metaclass__ = APIList_Metaclass(models.AttributeType,   serializers.AttributeTypeSerializer)
class DerangementTypeList : __metaclass__ = APIList_Metaclass(models.DerangementType, serializers.DerangementTypeSerializer)
class FlawTypeList        : __metaclass__ = APIList_Metaclass(models.FlawType,        serializers.FlawTypeSerializer)
class MeritTypeList       : __metaclass__ = APIList_Metaclass(models.MeritType,       serializers.MeritTypeSerializer)
class SkillTypeList       : __metaclass__ = APIList_Metaclass(models.SkillType,       serializers.SkillTypeSerializer)

class AffiliationList   : __metaclass__ = APIList_Metaclass(models.Affiliation,   serializers.AffiliationSerializer)
class AttributeList     : __metaclass__ = APIList_Metaclass(models.Attribute,     serializers.AttributeSerializer)
class CharacterTextList : __metaclass__ = APIList_Metaclass(models.CharacterText, serializers.CharacterTextSerializer)
class CombatTraitList   : __metaclass__ = APIList_Metaclass(models.CombatTrait,   serializers.CombatTraitSerializer)
class CreatureTypeList  : __metaclass__ = APIList_Metaclass(models.CreatureType,  serializers.CreatureTypeSerializer)
class DerangementList   : __metaclass__ = APIList_Metaclass(models.Derangement,   serializers.DerangementSerializer)
class FlawList          : __metaclass__ = APIList_Metaclass(models.Flaw,          serializers.FlawSerializer)
class GenealogyList     : __metaclass__ = APIList_Metaclass(models.Genealogy,     serializers.GenealogySerializer)
class MeritList         : __metaclass__ = APIList_Metaclass(models.Merit,         serializers.MeritSerializer)
class MiscTraitList     : __metaclass__ = APIList_Metaclass(models.MiscTrait,     serializers.MiscTraitSerializer)
class PowerList         : __metaclass__ = APIList_Metaclass(models.Power,         serializers.PowerSerializer)
class SkillList         : __metaclass__ = APIList_Metaclass(models.Skill,         serializers.SkillSerializer)
class SubgroupList      : __metaclass__ = APIList_Metaclass(models.Subgroup,      serializers.SubgroupSerializer)
class ViceList          : __metaclass__ = APIList_Metaclass(models.Vice,          serializers.ViceSerializer)
class VirtueList        : __metaclass__ = APIList_Metaclass(models.Virtue,        serializers.VirtueSerializer)


# # # # # # # # # # # # # # # #
# Generate BackboneJS models  #
# # # # # # # # # # # # # # # #

def generate_enum (request, enum_name):
    Model = get_model('traits', enum_name)
    model_name = Model._meta.object_name
    serializer = getattr(serializers, model_name + 'Serializer')(
        Model.objects.all(),
        many = True
    )
    return render(request, 'traits/trait_enum.js', {
        'enum_name'   : model_name,
        'values_json' : JSONRenderer().render(serializer.data),
    }, content_type = 'text/javascript')

def generate_trait_model (request, trait_name):
    Model = get_model('traits', trait_name)
    return render(request, 'trait_model_template.js', {
        'model_name' : Model._meta.object_name,
        'Model'      : Model,
    }, content_type = 'text/javascript')
