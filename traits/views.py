from rest_framework import generics

import traits.models as trait_models
import traits.serializers as trait_serializers


def create_api_list(model_name):
    return type(
        model_name + 'List',
        (generics.ListCreateAPIView,),
        dict(
            model            = getattr(trait_models, model_name),
            serializer_class = getattr(trait_serializers, model_name + 'Serializer')
        )
    )

def create_api_detail(model_name):
    return type(
        model_name + 'Detail',
        (generics.RetrieveUpdateDestroyAPIView,),
        dict(
            model            = getattr(trait_models, model_name),
            serializer_class = getattr(trait_serializers, model_name + 'Serializer')
        )
    )


AttributeTypeList   = create_api_list('AttributeType');   AttributeTypeDetail   = create_api_detail('AttributeType')
DerangementTypeList = create_api_list('DerangementType'); DerangementTypeDetail = create_api_detail('DerangementType')
FlawTypeList        = create_api_list('FlawType');        FlawTypeDetail        = create_api_detail('FlawType')
SkillTypeList       = create_api_list('SkillType');       SkillTypeDetail       = create_api_detail('SkillType')

AttributeList   = create_api_list('Attribute');   AttributeDetail   = create_api_detail('Attribute')
CombatTraitList = create_api_list('CombatTrait'); CombatTraitDetail = create_api_detail('CombatTrait')
DerangementList = create_api_list('Derangement'); DerangementDetail = create_api_detail('Derangement')
FlawList        = create_api_list('Flaw');        FlawDetail        = create_api_detail('Flaw')
SkillList       = create_api_list('Skill');       SkillDetail       = create_api_detail('Skill')
