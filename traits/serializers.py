from rest_framework import serializers

import traits


def create_serializer(model_name):
    Meta = type(
        'Meta',
        (object,),
        dict(model = getattr(traits.models, model_name))
    )
    return type(
        model_name + 'Serializer',
        (serializers.ModelSerializer,),
        dict(Meta = Meta)
    )


AttributeTypeSerializer   = create_serializer('AttributeType')
DerangementTypeSerializer = create_serializer('DerangementType')
FlawTypeSerializer        = create_serializer('FlawType')
SkillTypeSerializer       = create_serializer('SkillType')

AttributeSerializer   = create_serializer('Attribute')
CombatTraitSerializer = create_serializer('CombatTrait')
DerangementSerializer = create_serializer('Derangement')
FlawSerializer        = create_serializer('Flaw')
SkillSerializer       = create_serializer('Skill')
