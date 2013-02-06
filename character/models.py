from django.db import models
from django.contrib.auth.models import User

import traits.models as trait_models

_character_trait_models = []


class Character(models.Model):
    enabled = models.BooleanField(default = True)
    user    = models.ForeignKey(User)
    # chronicle = models.ForeignKey(Chronicle)
    # status = models.EnumField()

    name          = models.CharField(blank = True, max_length = 256)
    creature_type = models.ForeignKey(trait_models.CreatureType)
    genealogy     = models.ForeignKey(trait_models.Genealogy)
    affiliation   = models.ForeignKey(trait_models.Affiliation)
    subgroup      = models.ForeignKey(trait_models.Subgroup)
    virtue        = models.ForeignKey(trait_models.Virtue)
    vice          = models.ForeignKey(trait_models.Vice)
    texts         = models.ManyToManyField(trait_models.CharacterText, through = 'CharacterHasText')

    date_created     = models.DateTimeField(auto_now_add = True)
    date_submitted   = models.DateTimeField(null = True, blank = True)
    date_approved    = models.DateTimeField(null = True, blank = True)
    date_last_edited = models.DateTimeField(auto_now = True)

    attributes          = models.ManyToManyField(trait_models.Attribute,    through = 'CharacterHasAttribute')
    skills              = models.ManyToManyField(trait_models.Skill,        through = 'CharacterHasSkill')
    skill_specialties   = models.ManyToManyField(trait_models.Skill,        through = 'CharacterHasSkillSpecialty', related_name = 'character_specialties_set')
    powers              = models.ManyToManyField(trait_models.Power,        through = 'CharacterHasPower')
    merits              = models.ManyToManyField(trait_models.Merit,        through = 'CharacterHasMerit')
    flaws               = models.ManyToManyField(trait_models.Flaw,         through = 'CharacterHasFlaw')
    derangements        = models.ManyToManyField(trait_models.Derangement,  through = 'CharacterHasDerangement')
    combat_traits       = models.ManyToManyField(trait_models.CombatTrait,  through = 'CharacterHasCombatTrait')
    misc_traits         = models.ManyToManyField(trait_models.MiscTrait,    through = 'CharacterHasMiscTrait')


class CharacterHasText(models.Model):
    character = models.ForeignKey(Character)
    attribute = models.ForeignKey(trait_models.CharacterText)
    text      = models.TextField(blank = True)
_character_trait_models.append(CharacterHasText)


class CharacterHasAttribute(models.Model):
    character = models.ForeignKey(Character)
    attribute = models.ForeignKey(trait_models.Attribute)
    rating    = models.SmallIntegerField(default = 1)
_character_trait_models.append(CharacterHasAttribute)


class CharacterHasSkill(models.Model):
    character = models.ForeignKey(Character)
    skill     = models.ForeignKey(trait_models.Skill)
    rating    = models.SmallIntegerField()
_character_trait_models.append(CharacterHasSkill)


class CharacterHasSkillSpecialty(models.Model):
    character       = models.ForeignKey(Character)
    skill_specialty = models.ForeignKey(trait_models.Skill)
    specialty       = models.CharField(max_length = 256)
_character_trait_models.append(CharacterHasSkillSpecialty)


class CharacterHasPower(models.Model):
    character = models.ForeignKey(Character)
    power = models.ForeignKey(trait_models.Power)
_character_trait_models.append(CharacterHasPower)


class CharacterHasMerit(models.Model):
    character     = models.ForeignKey(Character)
    merit         = models.ForeignKey(trait_models.Merit)
    rating        = models.SmallIntegerField()
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasMerit)


class CharacterHasFlaw(models.Model):
    character     = models.ForeignKey(Character)
    flaw          = models.ForeignKey(trait_models.Flaw)
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasFlaw)


class CharacterHasDerangement(models.Model):
    character     = models.ForeignKey(Character)
    derangement   = models.ForeignKey(trait_models.Derangement)
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasDerangement)


class CharacterHasCombatTrait(models.Model):
    character    = models.ForeignKey(Character)
    combat_trait = models.ForeignKey(trait_models.CombatTrait)
    rating       = models.SmallIntegerField()
_character_trait_models.append(CharacterHasCombatTrait)


class CharacterHasMiscTrait(models.Model):
    character   = models.ForeignKey(Character)
    misc_trait  = models.ForeignKey(trait_models.MiscTrait)
    rating      = models.SmallIntegerField()
    description = models.TextField(null = True, blank = True)
_character_trait_models.append(CharacterHasMiscTrait)
