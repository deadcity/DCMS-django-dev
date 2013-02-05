from django.db import models

_enum_models = []
_trait_models = []


class Enum(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class AttributeType   (Enum): pass
class DerangementType (Enum): pass
class FlawType        (Enum): pass
class MeritType       (Enum): pass
class SkillType       (Enum): pass

_enum_models.append(AttributeType)
_enum_models.append(DerangementType)
_enum_models.append(FlawType)
_enum_models.append(MeritType)
_enum_models.append(SkillType)


class Trait(models.Model):
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name


class Attribute(Trait):
    type = models.ForeignKey(AttributeType)
_trait_models.append(Attribute)


class CombatTrait(Trait):
    pass
_trait_models.append(CombatTrait)


class Derangement(Trait):
    type = models.ForeignKey(DerangementType)
    requires_specification = models.BooleanField()
_trait_models.append(Derangement)


class Flaw(Trait):
    type = models.ForeignKey(FlawType)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()
_trait_models.append(Flaw)


class Skill(Trait):
    type = models.ForeignKey(SkillType)
_trait_models.append(Skill)
