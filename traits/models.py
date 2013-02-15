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

class EnumField(models.ForeignKey): pass


class Trait(models.Model):
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 256, unique = True)

    def __unicode__(self):
        return self.name

    fields = [
        { 'name': 'enabled', 'type': models.BooleanField },
        { 'name': 'name',    'type': models.CharField },
    ]


class Affiliation(Trait): pass
_trait_models.append(Affiliation)


class Attribute(Trait):
    type = EnumField(AttributeType)

    fields = Trait.fields + [
        { 'name': 'type', 'type': EnumField },
    ]
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

    fields = Trait.fields + [
        {'name': 'genealogy_name',   'type': models.CharField },
        {'name': 'affiliation_name', 'type': models.CharField },
        {'name': 'subgroup_name',    'type': models.CharField },
        {'name': 'power_name',       'type': models.CharField },
    ]
_trait_models.append(CreatureType)


class Derangement(Trait):
    type = EnumField(DerangementType)
    requires_specification = models.BooleanField()

    fields = Trait.fields + [
        { 'name': 'type',                   'type': EnumField },
        { 'name': 'requires_specification', 'type': models.BooleanField },
    ]
_trait_models.append(Derangement)


class Flaw(Trait):
    type = EnumField(FlawType)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()

    fields = Trait.fields + [
        { 'name': 'type',                   'type': EnumField },
        { 'name': 'requires_specification', 'type': models.BooleanField },
        { 'name': 'requires_description',   'type': models.BooleanField },
    ]
_trait_models.append(Flaw)


class Genealogy(Trait): pass
_trait_models.append(Genealogy)


class Merit(Trait):
    type = EnumField(MeritType)
    min_rating = models.SmallIntegerField()
    max_rating = models.SmallIntegerField()
    inc_rating = models.SmallIntegerField()
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()

    fields = Trait.fields + [
        { 'name': 'type',                   'type': EnumField },
        { 'name': 'min_rating',             'type': models.SmallIntegerField },
        { 'name': 'max_rating',             'type': models.SmallIntegerField },
        { 'name': 'inc_rating',             'type': models.SmallIntegerField },
        { 'name': 'requires_specification', 'type': models.BooleanField },
        { 'name': 'requires_description',   'type': models.BooleanField },
    ]
_trait_models.append(Merit)


class MiscTrait(Trait):
    requires_description = models.BooleanField()

    fields = Trait.fields + [
        { 'name': 'requires_description',   'type': models.BooleanField },
    ]
_trait_models.append(MiscTrait)


class Power(Trait):
    rating = models.IntegerField()
    group  = models.CharField(max_length = 256, null = True, blank = True)

    def __unicode__(self):
        if self.name is None or self.name == '':
            return self.group + ' ' + unicode(self.rating)
        else:
            return name

    fields = Trait.fields + [
        { 'name': 'rating', 'type': models.IntegerField },
        { 'name': 'group',  'type': models.CharField },
    ]
_trait_models.append(Power)


class Skill(Trait):
    type = EnumField(SkillType)

    fields = Trait.fields + [
        { 'name': 'type', 'type': EnumField },
    ]
_trait_models.append(Skill)


class Subgroup(Trait): pass
_trait_models.append(Subgroup)
