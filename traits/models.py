from django.db import models

from common.metaclasses import Model_Metaclass


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


class Attribute(Trait):
    type = EnumField(AttributeType, related_name = 'trait', null = True)


class CharacterText(Trait):
    hide_from_player = models.BooleanField(default = False)


class CombatTrait(Trait): pass


class CreatureType(Trait):
    genealogy_name   = models.CharField(max_length = 256, null = True, blank = True)
    affiliation_name = models.CharField(max_length = 256, null = True, blank = True)
    subgroup_name    = models.CharField(max_length = 256, null = True, blank = True)
    power_name       = models.CharField(max_length = 256, null = True, blank = True)


class Derangement(Trait):
    type = EnumField(DerangementType, related_name = 'trait', null = True)
    requires_specification = models.BooleanField()


class Flaw(Trait):
    type = EnumField(FlawType, related_name = 'trait', null = True)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()


class Genealogy(Trait): pass


class Merit(Trait):
    type = EnumField(MeritType, related_name = 'trait', null = True)
    min_rating = models.SmallIntegerField()
    max_rating = models.SmallIntegerField()
    inc_rating = models.SmallIntegerField()
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()


class MiscTrait(Trait):
    requires_description = models.BooleanField()


class Power(Trait):
    rating = models.IntegerField(null = True, blank = True)
    group  = models.CharField(max_length = 256)


class Skill(Trait):
    type = EnumField(SkillType, related_name = 'trait', null = True)
    class Meta(object):
        ordering = ('name',)


class Subgroup(Trait): pass
