from django.db import models

from common.metaclasses import Model_Metaclass


class EnumModel(models.Model):
    __metaclass__ = Model_Metaclass
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

    class Meta(object):
        abstract = True


class AttributeType   (EnumModel): pass
class DerangementType (EnumModel): pass
class FlawType        (EnumModel): pass
class MeritType       (EnumModel): pass
class SkillType       (EnumModel): pass
class Vice            (EnumModel): pass
class Virtue          (EnumModel): pass


class EnumModelKey(models.ForeignKey): pass


class TraitModel(models.Model):
    __metaclass__ = Model_Metaclass
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 255, unique = True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        abstract = True


class Affiliation(TraitModel): pass


class Attribute(TraitModel):
    type = EnumModelKey(AttributeType, related_name = 'trait', null = True)


class CharacterText(TraitModel):
    hide_from_player = models.BooleanField(default = False)


class CombatTrait(TraitModel): pass


class CreatureType(TraitModel):
    genealogy_name   = models.CharField(max_length = 255, null = True, blank = True)
    affiliation_name = models.CharField(max_length = 255, null = True, blank = True)
    subgroup_name    = models.CharField(max_length = 255, null = True, blank = True)
    power_name       = models.CharField(max_length = 255, null = True, blank = True)


class Derangement(TraitModel):
    type = EnumModelKey(DerangementType, related_name = 'trait', null = True)
    requires_specification = models.BooleanField()


class Flaw(TraitModel):
    type = EnumModelKey(FlawType, related_name = 'trait', null = True)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()


class Genealogy(TraitModel): pass


class Merit(TraitModel):
    type = EnumModelKey(MeritType, related_name = 'trait', null = True)
    allowed_ratings        = models.CommaSeparatedIntegerField(max_length = 255)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()


class MiscTrait(TraitModel):
    requires_description = models.BooleanField()


class Power(TraitModel):
    rating = models.IntegerField(null = True, blank = True)
    group  = models.CharField(max_length = 255)


class Skill(TraitModel):
    type = EnumModelKey(SkillType, related_name = 'trait', null = True)
    class Meta(object):
        ordering = ('name',)

class Subgroup(TraitModel): pass
