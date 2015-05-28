## @module characters.models
#  Provides models pertaining to storing a character.


from datetime import datetime
from enum import Enum

from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import CheckConstraint, Column, ForeignKey, UniqueConstraint
from sqlalchemy.sql.expression import or_
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

    id = Column(Integer, primary_key = True)

    enabled = Column(Boolean, nullable = False, default = True)
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

    def __unicode__(self):
        return self.name

    user      = relationship(User)
    # chronicle = relationship(Chronicle)

    creature_type = relationship(trait_models.CreatureType)
    genealogy     = relationship(trait_models.Genealogy)
    affiliation   = relationship(trait_models.Affiliation)
    subgroup      = relationship(trait_models.Subgroup)
    virtue        = relationship(trait_models.Virtue)
    vice          = relationship(trait_models.Vice)

    attributes        = relationship('CharacterHasAttribute')
    skills            = relationship('CharacterHasSkill')
    skill_specialties = relationship('CharacterHasSkillSpecialty')
    powers            = relationship('CharacterHasPower')
    merits            = relationship('CharacterHasMerit')
    flaws             = relationship('CharacterHasFlaw')
    derangements      = relationship('CharacterHasDerangement')
    combat_traits     = relationship('CharacterHasCombatTrait')
    misc_traits       = relationship('CharacterHasMiscTrait')


# class XPRecord (models.Model):
#     game      = models.ForeignKey(Game)
#     character = models.ForeignKey(Character)
#     amount    = models.SmallIntegerField()
#     note      = models.CharField(max_length = 255)

#     class Meta (object):
#         ordering = ('game__date', 'character')


class CharacterHasTrait (AppLabel, BaseModel):
    def __repr__ (self):
        return "<{}({}, {}, {})>".format(
            type(self).__name__,
            '(un-named chronicle)' if not self.character.chronicle
                else self.character.chronicle.name,
            self.character.name,
            self.trait.name
        )

    id = Column(Integer, primary_key = True)
    _discriminator = Column(String, nullable = False)

    character_id = Column(Integer, ForeignKey(Character.id),          nullable = False)
    trait_id     = Column(Integer, ForeignKey(trait_models.Trait.id), nullable = False)

    # TODO(Emery): Limit the value of `_discriminator` to enforce using the
    #              appropriate child class when linking to the appropriate type
    #              of trait.
    # possible solution: composite foreign key using ForeignKeyConstraint
    #      e.g. ForeignKeyConstraint(
    #               (trait_id, _discriminator),
    #               (Trait.id, Trait._discriminator)
    #           )
    #    (This won't work right now.  It will break skill-specialties.)

    __mapper_args__ = {
        'polymorphic_on': _discriminator,
    }

    character = relationship(Character)
    trait     = relationship(trait_models.Trait, lazy = 'joined')


class CharacterHasAttribute (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating = Column(SmallInteger, nullable = False, default = 1)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
        CheckConstraint(rating > 0, name = 'positive_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'attribute',
    }


class CharacterHasCharacterText (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    text = Column(Text, nullable = False, default = '')

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'character_text',
    }


class CharacterHasCombatTrait (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating = Column(SmallInteger)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'combat_trait',
    }


class CharacterHasDerangement (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    specification = Column(String)
    description   = Column(Text)

    __mapper_args__ = {
        'polymorphic_identity': 'derangement',
    }


class CharacterHasFlaw (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating        = Column(SmallInteger)
    specification = Column(String)
    description   = Column(Text)

    __table_args__ = (
        CheckConstraint(or_(rating == None, rating > 0), name = 'positive_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'flaw',
    }


class CharacterHasMerit (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating        = Column(SmallInteger, nullable = False)
    specification = Column(String)
    description   = Column(Text)

    __table_args__ = (CheckConstraint(rating > 0, name = 'positive_rating'),)

    __mapper_args__ = {
        'polymorphic_identity': 'merit',
    }


class CharacterHasMiscTrait (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating      = Column(SmallInteger, nullable = False)
    description = Column(Text)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
        CheckConstraint(rating >= 0, name = 'non_negative_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'misc_trait',
    }


class CharacterHasPower (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'power',
    }


class CharacterHasSkill (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating = Column(SmallInteger, nullable = False, default = 0)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
        CheckConstraint(rating >= 0, name = 'non_negative_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'skill',
    }


class CharacterHasSkillSpecialty (CharacterHasTrait):
    id = Column(Integer, ForeignKey(CharacterHasTrait.id, ondelete = 'CASCADE'), primary_key = True)

    specialty = Column(String, nullable = False)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id, specialty),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'skill_specialty',
    }
