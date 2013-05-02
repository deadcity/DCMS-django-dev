from django.db import models

from common.generators import Model_Metaclass

_enum_models = []
_trait_models = []


class Enum(models.Model):
    __metaclass__ = Model_Metaclass
    name = models.CharField(max_length = 256)

    def __unicode__(self):
        return self.name

    class Meta(object):
        abstract = True


class AttributeType   (Enum): pass
class DerangementType (Enum): pass
class FlawType        (Enum): pass
class MeritType       (Enum): pass
class SkillType       (Enum): pass
class Vice            (Enum): pass
class Virtue          (Enum): pass

_enum_models.append(AttributeType)
_enum_models.append(DerangementType)
_enum_models.append(FlawType)
_enum_models.append(MeritType)
_enum_models.append(SkillType)
_enum_models.append(Vice)
_enum_models.append(Virtue)

class EnumField(models.ForeignKey): pass


class Trait(models.Model):
    __metaclass__ = Model_Metaclass
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 256, unique = True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        abstract = True


class Affiliation(Trait): pass
_trait_models.append(Affiliation)


class Attribute(Trait):
    type = EnumField(AttributeType, null = True)
_trait_models.append(Attribute)


class CharacterText(Trait):
    hide_from_player = models.BooleanField(default = False)
_trait_models.append(CharacterText)


class CombatTrait(Trait): pass
_trait_models.append(CombatTrait)


class CreatureType(Trait):
    genealogy_name   = models.CharField(max_length = 256, null = True, blank = True)
    affiliation_name = models.CharField(max_length = 256, null = True, blank = True)
    subgroup_name    = models.CharField(max_length = 256, null = True, blank = True)
    power_name       = models.CharField(max_length = 256, null = True, blank = True)
_trait_models.append(CreatureType)


class Derangement(Trait):
    type = EnumField(DerangementType, null = True)
    requires_specification = models.BooleanField()
_trait_models.append(Derangement)


class Flaw(Trait):
    type = EnumField(FlawType, null = True)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()
_trait_models.append(Flaw)


class Genealogy(Trait): pass
_trait_models.append(Genealogy)


class Merit(Trait):
    type = EnumField(MeritType, null = True)
    min_rating = models.SmallIntegerField()
    max_rating = models.SmallIntegerField()
    inc_rating = models.SmallIntegerField()
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()
_trait_models.append(Merit)


class MiscTrait(Trait):
    requires_description = models.BooleanField()
_trait_models.append(MiscTrait)


class Power(Trait):
    rating = models.IntegerField(null = True, blank = True)
    group  = models.CharField(max_length = 256)
_trait_models.append(Power)


class Skill(Trait):
    type = EnumField(SkillType, null = True)
_trait_models.append(Skill)


class Subgroup(Trait): pass
_trait_models.append(Subgroup)
