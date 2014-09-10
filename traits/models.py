from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class TraitTypeModel (models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

    class Meta (object):
        abstract = True


class AttributeType   (TraitTypeModel): pass
class DerangementType (TraitTypeModel): pass
class FlawType        (TraitTypeModel): pass
class MeritType       (TraitTypeModel): pass
class SkillType       (TraitTypeModel): pass
class Vice            (TraitTypeModel): pass
class Virtue          (TraitTypeModel): pass


class TraitTypeField (models.ForeignKey):
    def __init__ (self, related, **kwargs):
        return super(TraitTypeField, self).__init__(related, related_name = 'trait', **kwargs)


class TraitModel (models.Model):
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 255, unique = True)

    def __unicode__(self):
        return self.name

    class Meta (object):
        abstract = True


class Affiliation (TraitModel): pass


class Attribute (TraitModel):
    type = TraitTypeField(AttributeType)


class CharacterText (TraitModel):
    hide_from_player = models.BooleanField(default = False)


class CombatTrait (TraitModel): pass


class CreatureType (TraitModel):
    genealogy_name   = models.CharField(max_length = 255, null = True, blank = True)
    affiliation_name = models.CharField(max_length = 255, null = True, blank = True)
    subgroup_name    = models.CharField(max_length = 255, null = True, blank = True)
    power_name       = models.CharField(max_length = 255, null = True, blank = True)


class Derangement (TraitModel):
    type = TraitTypeField(DerangementType)
    requires_specification = models.BooleanField()


class Flaw (TraitModel):
    type = TraitTypeField(FlawType, null = True)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()


class Genealogy (TraitModel): pass


class Merit (TraitModel):
    type = TraitTypeField(MeritType, null = True)
    allowed_ratings        = models.CommaSeparatedIntegerField(max_length = 255)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()


class MiscTrait (TraitModel):
    requires_description = models.BooleanField()


class PowerGroup(Trait): pass


class Power (TraitModel):
    rating = models.IntegerField(null = True, blank = True)
    group  = models.CharField(max_length = 255)

    def __unicode__ (self):
        return '{} {} - {}'.format(self.group, self.rating, self.name)


class CreatureTypeHasPowerGroup(Trait):
    creature_type = models.ForeignKey(CreatureType)
    power_group = models.ForeignKey(PowerGroup)


class CreatureTypeHasGenealogy(Trait):
    creature_type = models.ForeignKey(CreatureType)
    genealogy = models.ForeignKey(Genealogy)
    

class CreatureTypeHasAffiliation(Trait):
    creature_type = models.ForeignKey(CreatureType)
    affiliation = models.ForeignKey(Affiliation)
    

class CreatureTypeHasMerit(Trait):
    creature_type = models.ForeignKey(CreatureType)
    merit = models.ForeignKey(Merit)


class Skill (TraitModel):
    type = TraitTypeField(SkillType)


class Subgroup (TraitModel): pass
