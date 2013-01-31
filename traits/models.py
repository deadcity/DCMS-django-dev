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


class SkillType(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name


class Skill(Trait):
    type = models.ForeignKey(SkillType)
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

