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

    attributes          = models.ManyToManyField(trait_models.Attribute,    through = 'CharacterHasAttribute')
    skills              = models.ManyToManyField(trait_models.Skill,        through = 'CharacterHasSkill')
    skill_specialties   = models.ManyToManyField(trait_models.Skill,        through = 'CharacterHasSkillSpecialty', related_name = 'character_specialties_set')
    powers              = models.ManyToManyField(trait_models.Power,        through = 'CharacterHasPower')
    merits              = models.ManyToManyField(trait_models.Merit,        through = 'CharacterHasMerit')
    flaws               = models.ManyToManyField(trait_models.Flaw,         through = 'CharacterHasFlaw')
    derangements        = models.ManyToManyField(trait_models.Derangement,  through = 'CharacterHasDerangement')
    combat_traits       = models.ManyToManyField(trait_models.CombatTrait,  through = 'CharacterHasCombatTrait')
    misc_traits         = models.ManyToManyField(trait_models.MiscTrait,    through = 'CharacterHasMiscTrait')

    def __unicode__(self):
        return self.name


class CharacterHasTrait(models.Model):
    character = models.ForeignKey(Character)
    class Meta(object):
        abstract = True

    fields = [
    ]


class CharacterHasText(CharacterHasTrait):
    character_text = models.ForeignKey(trait_models.CharacterText)
    text           = models.TextField(blank = True)
    class Meta(object):
        unique_together = ('character', 'character_text')

    fields = CharacterHasTrait.fields + [
        'character_text',
        'text',
    ]
_character_trait_models.append(CharacterHasText)


class CharacterHasAttribute(CharacterHasTrait):
    attribute = models.ForeignKey(trait_models.Attribute)
    rating    = models.SmallIntegerField(default = 1)
    class Meta(object):
        unique_together = ('character', 'attribute')

    fields = CharacterHasTrait.fields + [
        'attribute',
        'rating',
    ]
_character_trait_models.append(CharacterHasAttribute)


class CharacterHasSkill(CharacterHasTrait):
    skill  = models.ForeignKey(trait_models.Skill)
    rating = models.SmallIntegerField()
    class Meta(object):
        unique_together = ('character', 'skill')

    fields = CharacterHasTrait.fields + [
        'skill',
        'rating',
    ]
_character_trait_models.append(CharacterHasSkill)


class CharacterHasSkillSpecialty(CharacterHasTrait):
    skill     = models.ForeignKey(trait_models.Skill)
    specialty = models.CharField(max_length = 256)
    class Meta(object):
        unique_together = ('character', 'skill', 'specialty')

    fields = CharacterHasTrait.fields + [
        'skill',
        'specialty',
    ]
_character_trait_models.append(CharacterHasSkillSpecialty)


class CharacterHasPower(CharacterHasTrait):
    power = models.ForeignKey(trait_models.Power)
    class Meta(object):
        unique_together = ('character', 'power')

    fields = CharacterHasTrait.fields + [
        'power',
    ]
_character_trait_models.append(CharacterHasPower)


class CharacterHasMerit(CharacterHasTrait):
    merit         = models.ForeignKey(trait_models.Merit)
    rating        = models.SmallIntegerField()
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)

    fields = CharacterHasTrait.fields + [
        'merit',
        'rating',
        'specification',
        'description',
    ]
_character_trait_models.append(CharacterHasMerit)


class CharacterHasFlaw(CharacterHasTrait):
    flaw          = models.ForeignKey(trait_models.Flaw)
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)

    fields = CharacterHasTrait.fields + [
        'flaw',
        'specification',
        'description',
    ]
_character_trait_models.append(CharacterHasFlaw)


class CharacterHasDerangement(CharacterHasTrait):
    derangement   = models.ForeignKey(trait_models.Derangement)
    specification = models.CharField(null = True, blank = True, max_length = 256)
    description   = models.TextField(null = True, blank = True)

    fields = CharacterHasTrait.fields + [
        'derangement',
        'specification',
        'description',
    ]
_character_trait_models.append(CharacterHasDerangement)


class CharacterHasCombatTrait(CharacterHasTrait):
    combat_trait = models.ForeignKey(trait_models.CombatTrait)
    rating       = models.SmallIntegerField()
    class Meta(object):
        unique_together = ('character', 'combat_trait')

    fields = CharacterHasTrait.fields + [
        'combat_trait',
        'rating',
    ]
_character_trait_models.append(CharacterHasCombatTrait)


class CharacterHasMiscTrait(CharacterHasTrait):
    misc_trait  = models.ForeignKey(trait_models.MiscTrait)
    rating      = models.SmallIntegerField()
    description = models.TextField(null = True, blank = True)

    fields = CharacterHasTrait.fields + [
        'misc_trait',
        'rating',
        'description',
    ]
_character_trait_models.append(CharacterHasMiscTrait)
