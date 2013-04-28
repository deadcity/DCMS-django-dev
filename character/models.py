from django.db import models
from django.contrib.auth.models import User

from common.generators import Model_Metaclass
import traits.models as trait_models

_character_trait_models = []


class Character(models.Model):
    __metaclass__ = Model_Metaclass

    enabled = models.BooleanField(default = True)
    user    = models.ForeignKey(User)
    # chronicle = models.ForeignKey(Chronicle)
    # status = models.EnumField()

    name          = models.CharField(blank = True, max_length = 256)
    creature_type = models.ForeignKey(trait_models.CreatureType, null = True, blank = True)
    genealogy     = models.ForeignKey(trait_models.Genealogy,    null = True, blank = True)
    affiliation   = models.ForeignKey(trait_models.Affiliation,  null = True, blank = True)
    subgroup      = models.ForeignKey(trait_models.Subgroup,     null = True, blank = True)
    virtue        = models.ForeignKey(trait_models.Virtue,       null = True, blank = True)
    vice          = models.ForeignKey(trait_models.Vice,         null = True, blank = True)
    texts         = models.ManyToManyField(trait_models.CharacterText, through = 'CharacterHasText')

    date_created     = models.DateTimeField(auto_now_add = True)
    date_submitted   = models.DateTimeField(null = True, blank = True)
    date_approved    = models.DateTimeField(null = True, blank = True)
    date_last_edited = models.DateTimeField(auto_now = True)

    attributes        = models.ManyToManyField(trait_models.Attribute,   through = 'CharacterHasAttribute')
    skills            = models.ManyToManyField(trait_models.Skill,       through = 'CharacterHasSkill')
    skill_specialties = models.ManyToManyField(trait_models.Skill,       through = 'CharacterHasSkillSpecialty', related_name = 'character_specialties_set')
    powers            = models.ManyToManyField(trait_models.Power,       through = 'CharacterHasPower')
    merits            = models.ManyToManyField(trait_models.Merit,       through = 'CharacterHasMerit')
    flaws             = models.ManyToManyField(trait_models.Flaw,        through = 'CharacterHasFlaw')
    derangements      = models.ManyToManyField(trait_models.Derangement, through = 'CharacterHasDerangement')
    combat_traits     = models.ManyToManyField(trait_models.CombatTrait, through = 'CharacterHasCombatTrait')
    misc_traits       = models.ManyToManyField(trait_models.MiscTrait,   through = 'CharacterHasMiscTrait')

    def __unicode__(self):
        return self.name


class CharacterHasTrait(models.Model):
    __metaclass__ = Model_Metaclass
    character = models.ForeignKey(Character)
    class Meta(object):
        abstract = True


class CharacterHasText(CharacterHasTrait):
    trait = models.ForeignKey(trait_models.CharacterText)
    text  = models.TextField(blank = True)
    class Meta(object):
        unique_together = ('character', 'trait')
_character_trait_models.append(CharacterHasText)


class CharacterHasAttribute(CharacterHasTrait):
    trait  = models.ForeignKey(trait_models.Attribute)
    rating = models.SmallIntegerField(default = 1)
    class Meta(object):
        unique_together = ('character', 'trait')
_character_trait_models.append(CharacterHasAttribute)


class CharacterHasSkill(CharacterHasTrait):
    trait  = models.ForeignKey(trait_models.Skill)
    rating = models.SmallIntegerField()
    class Meta(object):
        unique_together = ('character', 'trait')
_character_trait_models.append(CharacterHasSkill)


class CharacterHasSkillSpecialty(CharacterHasTrait):
    trait     = models.ForeignKey(trait_models.Skill)
    specialty = models.CharField(max_length = 256)
    class Meta(object):
        unique_together = ('character', 'trait', 'specialty')
_character_trait_models.append(CharacterHasSkillSpecialty)


class CharacterHasPower(CharacterHasTrait):
    trait = models.ForeignKey(trait_models.Power)
    class Meta(object):
        unique_together = ('character', 'trait')
_character_trait_models.append(CharacterHasPower)


class CharacterHasMerit(CharacterHasTrait):
    trait         = models.ForeignKey(trait_models.Merit)
    rating        = models.SmallIntegerField(null = True, blank = True)
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasMerit)


class CharacterHasFlaw(CharacterHasTrait):
    trait         = models.ForeignKey(trait_models.Flaw)
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasFlaw)


class CharacterHasDerangement(CharacterHasTrait):
    trait         = models.ForeignKey(trait_models.Derangement)
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasDerangement)


class CharacterHasCombatTrait(CharacterHasTrait):
    trait = models.ForeignKey(trait_models.CombatTrait)
    rating       = models.SmallIntegerField()
    class Meta(object):
        unique_together = ('character', 'trait')
_character_trait_models.append(CharacterHasCombatTrait)


class CharacterHasMiscTrait(CharacterHasTrait):
    trait  = models.ForeignKey(trait_models.MiscTrait)
    rating      = models.SmallIntegerField()
    description = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasMiscTrait)
