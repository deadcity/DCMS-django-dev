## @module characters.models
#  Provides models pertaining to storing a character.


from datetime import datetime
from enum import Enum

from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import CheckConstraint, Column, ForeignKey
from sqlalchemy.types import Boolean, DateTime, Integer, SmallInteger, String, Text

from DCMS.model_base import BaseModel

from auth.models import User
# from chronicle.models import Game
from dsqla.column_types import EnumColumn
from dsqla.models import app_label
import traits.models as trait_models


AppLabel = app_label('characters')


class Character (AppLabel, BaseModel):
    class Status (Enum):
        EDITING   = 1
        SUBMITTED = 2
        APPROVED  = 3
        ACTIVE    = 4
        DECEASED  = 5
        INACTIVE  = 6

    enabled = Column(Boolan, nullable = False, default = True)
    user_id = Column(Integer, ForeignKey(User.id))
    # chronicle_id = Column(Integer, ForeignKey(Chronicle.id))
    status = Column(EnumColumn(Status, name = 'character_status'), nullable = False, default = Status.EDITING)

    name             = Column(String, nullable = False, default = '')
    creature_type_id = Column(Integer, ForeignKey(trait_models.CreatureType.id))
    genealogy_id     = Column(Integer, ForeignKey(trait_models.Genealogy.id))
    affiliation_id   = Column(Integer, ForeignKey(trait_models.Affiliation.id))
    subgroup_id      = Column(Integer, ForeignKey(trait_models.Subgroup.id))
    virtue_id        = Column(Integer, ForeignKey(trait_models.Virtue.id))
    vice_id          = Column(Integer, ForeignKey(trait_models.Vice.id))

    date_created     = Column(DateTime, nullable = False, default = datetime.utcnow)
    date_submitted   = Column(DateTime)
    date_approved    = Column(DateTime)
    date_last_edited = Column(DateTime, nullable = False, default = datetime.utcnow, onupdate = datetime.utcnow)

    # attributes        = models.ManyToManyField(trait_models.Attribute,   through = 'CharacterHasAttribute')
    # skills            = models.ManyToManyField(trait_models.Skill,       through = 'CharacterHasSkill')
    # skill_specialties = models.ManyToManyField(trait_models.Skill,       through = 'CharacterHasSkillSpecialty', related_name = 'character_specialties_set')
    # powers            = models.ManyToManyField(trait_models.Power,       through = 'CharacterHasPower')
    # merits            = models.ManyToManyField(trait_models.Merit,       through = 'CharacterHasMerit')
    # flaws             = models.ManyToManyField(trait_models.Flaw,        through = 'CharacterHasFlaw')
    # derangements      = models.ManyToManyField(trait_models.Derangement, through = 'CharacterHasDerangement')
    # combat_traits     = models.ManyToManyField(trait_models.CombatTrait, through = 'CharacterHasCombatTrait')
    # misc_traits       = models.ManyToManyField(trait_models.MiscTrait,   through = 'CharacterHasMiscTrait')

    def __unicode__(self):
        return self.name

    creature_type = relationship(trait_models.CreatureType)
    genealogy     = relationship(trait_models.Genealogy)
    affiliation   = relationship(trait_models.Affiliation)
    subgroup      = relationship(trait_models.Subgroup)
    virtue        = relationship(trait_models.Virtue)
    vice          = relationship(trait_models.Vice)


# class XPRecord (models.Model):
#     game      = models.ForeignKey(Game)
#     character = models.ForeignKey(Character)
#     amount    = models.SmallIntegerField()
#     note      = models.CharField(max_length = 255)

#     class Meta (object):
#         ordering = ('game__date', 'character')


class CharacterHasAttribute (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),              nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Attribute.id), nullable = False)

    rating = Column(SmallInteger, CheckConstraint(rating > 0), nullable = False, default = 1)

    __table_args__ = (UniqueConstraint(character_id, trait_id),)

    character = relationship(Character, backref = backref('attributes'))
    trait     = relationship(trait_models.Attribute, lazy = 'joined')


class CharacterHasCombatTrait (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),                nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.CombatTrait.id), nullable = False)

    rating = Column(SmallInteger)

    __table_args__ = (UniqueConstraint(character_id, trait_id),)

    character = relationship(Character, backref = backref('combat_traits'))
    trait     = relationship(trait_models.CombatTrait, lazy = 'joined')


class CharacterHasDerangement (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),                nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Derangement.id), nullable = False)

    specification = Column(String)
    description   = Column(Text)

    character = relationship(Character, backref = backref('derangements'))
    trait     = relationship(trait_models.Derangement, lazy = 'joined')


class CharacterHasFlaw (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),         nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Flaw.id), nullable = False)

    specification = Column(String)
    description   = Column(Text)

    character = relationship(Character, backref = backref('flaws'))
    trait     = relationship(trait_models.Flaw, lazy = 'joined')


class CharacterHasMerit (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),          nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Merit.id), nullable = False)

    specification = Column(String)
    description   = Column(Text)

    character = relationship(Character, backref = backref('merits'))
    trait     = relationship(trait_models.Merit, lazy = 'joined')


class CharacterHasMiscTrait (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),              nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.MiscTrait.id), nullable = False)

    rating      = Column(SmallInteger)
    description = Column(Text)

    __table_args__ = (UniqueConstraint(character_id, trait_id),)

    character = relationship(Character, backref = backref('misc_traits'))
    trait     = relationship(trait_models.MiscTrait, lazy = 'joined')


class CharacterHasPower (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),          nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Power.id), nullable = False)

    __table_args__ = (UniqueConstraint(character_id, trait_id),)

    character = relationship(Character, backref = backref('powers'))
    trait     = relationship(trait_models.Power, lazy = 'joined')


class CharacterHasSkill (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),          nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Skill.id), nullable = False)

    rating = Column(SmallInteger, nullable = False, default = 0)

    __table_args__ = (UniqueConstraint(character_id, trait_id),)

    character = relationship(Character, backref = backref('skills'))
    trait     = relationship(trait_models.Skill, lazy = 'joined')


class CharacterHasSkillSpecialty (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),          nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Skill.id), nullable = False)

    specialty = Column(String, nullable = False)

    __table_args__ = (UniqueConstraint(character_id, trait_id, specialty),)

    character = relationship(Character, backref = backref('skill_secialties'))
    trait     = relationship(trait_models.Skill, lazy = 'joined')


class CharacterHasText (AppLabel, BaseModel):
    character_id = Column(Integer, ForeignKey(Character.id),                  nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.CharacterText.id), nullable = False)

    text = Column(Text, nullable = False, default = '')

    __table_args__ = (UniqueConstraint(character_id, trait_id),)

    character = relationship(Character, backref = backref('texts'))
    trait     = relationship(trait_models.CharacterText, lazy = 'joined')
