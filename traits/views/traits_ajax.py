# DCMS auto-generated file
# Fri, 15 Nov 2013 07:36:58 -0600 | 76d7f7fbf6828cdd7ee0efe7cc31671c

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)



from rest_framework import viewsets

from traits import models, serializers


class AttributeTypeViewSet (viewsets.ModelViewSet):
    model            = models.AttributeType
    serializer_class = serializers.AttributeTypeSerializer


class DerangementTypeViewSet (viewsets.ModelViewSet):
    model            = models.DerangementType
    serializer_class = serializers.DerangementTypeSerializer


class FlawTypeViewSet (viewsets.ModelViewSet):
    model            = models.FlawType
    serializer_class = serializers.FlawTypeSerializer


class MeritTypeViewSet (viewsets.ModelViewSet):
    model            = models.MeritType
    serializer_class = serializers.MeritTypeSerializer


class SkillTypeViewSet (viewsets.ModelViewSet):
    model            = models.SkillType
    serializer_class = serializers.SkillTypeSerializer


class ViceViewSet (viewsets.ModelViewSet):
    model            = models.Vice
    serializer_class = serializers.ViceSerializer


class VirtueViewSet (viewsets.ModelViewSet):
    model            = models.Virtue
    serializer_class = serializers.VirtueSerializer


class AffiliationViewSet (viewsets.ModelViewSet):
    model            = models.Affiliation
    serializer_class = serializers.AffiliationSerializer


class AttributeViewSet (viewsets.ModelViewSet):
    model            = models.Attribute
    serializer_class = serializers.AttributeSerializer


class CharacterTextViewSet (viewsets.ModelViewSet):
    model            = models.CharacterText
    serializer_class = serializers.CharacterTextSerializer


class CombatTraitViewSet (viewsets.ModelViewSet):
    model            = models.CombatTrait
    serializer_class = serializers.CombatTraitSerializer


class CreatureTypeViewSet (viewsets.ModelViewSet):
    model            = models.CreatureType
    serializer_class = serializers.CreatureTypeSerializer


class DerangementViewSet (viewsets.ModelViewSet):
    model            = models.Derangement
    serializer_class = serializers.DerangementSerializer


class FlawViewSet (viewsets.ModelViewSet):
    model            = models.Flaw
    serializer_class = serializers.FlawSerializer


class GenealogyViewSet (viewsets.ModelViewSet):
    model            = models.Genealogy
    serializer_class = serializers.GenealogySerializer


class MeritViewSet (viewsets.ModelViewSet):
    model            = models.Merit
    serializer_class = serializers.MeritSerializer


class MiscTraitViewSet (viewsets.ModelViewSet):
    model            = models.MiscTrait
    serializer_class = serializers.MiscTraitSerializer


class PowerViewSet (viewsets.ModelViewSet):
    model            = models.Power
    serializer_class = serializers.PowerSerializer


class SkillViewSet (viewsets.ModelViewSet):
    model            = models.Skill
    serializer_class = serializers.SkillSerializer


class SubgroupViewSet (viewsets.ModelViewSet):
    model            = models.Subgroup
    serializer_class = serializers.SubgroupSerializer


