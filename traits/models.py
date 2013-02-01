from django.db import models


class Trait(models.Model):
    enabled = models.BooleanField(default = True)


class AttributeType(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name


class Attribute(Trait):
    type = models.ForeignKey(AttributeType)
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name


class CombatTrait(Trait):
    pass


class DerangementType(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Derangement(Trait):
    type = models.ForeignKey(DerangementType)
    requires_specification = models.BooleanField()


class MeritFlawType(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Flaw(Trait):
    type = models.ForeignKey(MeritFlawType)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()


class SkillType(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name


class Skill(Trait):
    type = models.ForeignKey(SkillType)
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

