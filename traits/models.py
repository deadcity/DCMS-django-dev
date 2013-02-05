from django.db import models


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


class Trait(models.Model):
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name


class Attribute(Trait):
    type = models.ForeignKey(AttributeType)


class CombatTrait(Trait):
    pass


class Derangement(Trait):
    type = models.ForeignKey(DerangementType)
    requires_specification = models.BooleanField()


class Flaw(Trait):
    type = models.ForeignKey(FlawType)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()



class Skill(Trait):
    type = models.ForeignKey(SkillType)
