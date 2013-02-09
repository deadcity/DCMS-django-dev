from django.db import models

_enum_models = []
_trait_models = []


class Enum(models.Model):
    name = models.CharField(max_length = 256, unique = True)

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


class Trait(models.Model):
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 256, unique = True)

    def __unicode__(self):
        return self.name


class Affiliation(Trait): pass
_trait_models.append(Affiliation)


class Attribute(Trait):
    type = models.ForeignKey(AttributeType)
_trait_models.append(Attribute)


class CharacterText(Trait): pass
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
    type = models.ForeignKey(DerangementType)
    requires_specification = models.BooleanField()
_trait_models.append(Derangement)


class Flaw(Trait):
    type = models.ForeignKey(FlawType)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()
_trait_models.append(Flaw)


class Genealogy(Trait): pass
_trait_models.append(Genealogy)


class Merit(Trait):
    type = models.ForeignKey(MeritType)
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
    rating = models.IntegerField()
    group  = models.CharField(max_length = 256, null = True, blank = True)

    def __unicode__(self):
        if self.name is None or self.name == '':
            return self.group + ' ' + unicode(self.rating)
        else:
            return name
_trait_models.append(Power)


class Skill(Trait):
    type = models.ForeignKey(SkillType)
_trait_models.append(Skill)


class Subgroup(Trait): pass
_trait_models.append(Subgroup)
