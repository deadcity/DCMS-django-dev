from django.contrib.auth.models import User
from django.db import models

from chronicle.models import Game
from common.enum import Enum
from common.fields import EnumField
import traits.models as trait_models


class CharacterStatus (Enum):
    EDITING   = { 'value': 10, 'label': 'Editing'   }
    SUBMITTED = { 'value': 20, 'label': 'Submitted' }
    APPROVED  = { 'value': 30, 'label': 'Approved'  }
    ACTIVE    = { 'value': 40, 'label': 'Active'    }
    DECEASED  = { 'value': 50, 'label': 'Deceased'  }
    INACTIVE  = { 'value': 60, 'label': 'Inactive'  }


class Character (models.Model):
    enabled = models.BooleanField(default = True)
    user    = models.ForeignKey(User)
    # chronicle = models.ForeignKey(Chronicle)
    status = EnumField(CharacterStatus, db_type = 'INTEGER', blank = True, null = True)

    name          = models.CharField(blank = True, max_length = 255)
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


class XPRecord (models.Model):
    game      = models.ForeignKey(Game)
    character = models.ForeignKey(Character)
    amount    = models.SmallIntegerField()
    note      = models.CharField(max_length = 255)

    class Meta (object):
        ordering = ('game__date', 'character')


class CharacterHasTraitModel (models.Model):
    character = models.ForeignKey(Character)

    def __unicode__(self):
        return unicode(self.trait)

    class Meta (object):
        abstract = True


class CharacterHasAttribute (CharacterHasTraitModel):
    trait  = models.ForeignKey(trait_models.Attribute)
    rating = models.SmallIntegerField(default = 1)

    class Meta (object):
        unique_together = ('character', 'trait')
        ordering        = ('trait__type__name',)


class CharacterHasCombatTrait (CharacterHasTraitModel):
    trait  = models.ForeignKey(trait_models.CombatTrait)
    rating = models.SmallIntegerField(null = True, blank = True)

    class Meta (object):
        unique_together = ('character', 'trait')
        ordering        = ('trait__name',)


class CharacterHasDerangement (CharacterHasTraitModel):
    trait         = models.ForeignKey(trait_models.Derangement)
    specification = models.CharField(null = True, blank = True, max_length = 255)
    description   = models.TextField(null = True, blank = True)

    class Meta (object):
        ordering = ('trait__type__name', 'trait__name')


class CharacterHasFlaw (CharacterHasTraitModel):
    trait         = models.ForeignKey(trait_models.Flaw)
    specification = models.CharField(null = True, blank = True, max_length = 255)
    description   = models.TextField(null = True, blank = True)

    class Meta (object):
        ordering = ('trait__type__name', 'trait__name')


class CharacterHasMerit (CharacterHasTraitModel):
    trait         = models.ForeignKey(trait_models.Merit)
    rating        = models.SmallIntegerField(null = True, blank = True)
    specification = models.CharField(null = True, blank = True, max_length = 255)
    description   = models.TextField(null = True, blank = True)

    class Meta (object):
        ordering = ('trait__type__name', 'trait__name')


class CharacterHasMiscTrait (CharacterHasTraitModel):
    trait       = models.ForeignKey(trait_models.MiscTrait)
    rating      = models.SmallIntegerField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)

    class Meta (object):
        ordering = ('trait__name',)


class CharacterHasPower (CharacterHasTraitModel):
    trait = models.ForeignKey(trait_models.Power)

    class Meta (object):
        unique_together = ('character', 'trait')
        ordering        = ('trait__group', 'trait__rating', 'trait__name')


class CharacterHasSkill (CharacterHasTraitModel):
    trait  = models.ForeignKey(trait_models.Skill)
    rating = models.SmallIntegerField(default = 0)

    class Meta (object):
        unique_together = ('character', 'trait')
        ordering        = ('trait__type__name', 'trait__name')


class CharacterHasSkillSpecialty (CharacterHasTraitModel):
    trait     = models.ForeignKey(trait_models.Skill)
    specialty = models.CharField(max_length = 255)

    class Meta (object):
        unique_together = ('character', 'trait', 'specialty')
        ordering        = ('trait__type__name', 'trait__name')


class CharacterHasText (CharacterHasTraitModel):
    trait = models.ForeignKey(trait_models.CharacterText)
    text  = models.TextField(blank = True)

    class Meta (object):
        unique_together = ('character', 'trait')
        ordering        = ('trait__name',)
