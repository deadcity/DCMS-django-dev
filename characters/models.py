## @module characters.models
#  Provides models pertaining to storing a character.


from datetime import datetime
from enum import Enum

from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import CheckConstraint, Column, ForeignKey, UniqueConstraint
from sqlalchemy.sql.expression import or_
from sqlalchemy.types import Boolean, DateTime, Integer, SmallInteger, String, Text

from DCMS.model_base import BaseModel

from dsqla.column_types import EnumColumn
from dsqla.models import app_label


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

    enabled      = Column(Boolean, nullable = False, default = True)
    user_id      = Column(Integer, ForeignKey('auth_user.id'), nullable = False)
    chronicle_id = Column(Integer, ForeignKey('chronicles_chronicle.id'), nullable = False)
    status       = Column(EnumColumn(Status, name = 'character_status'), nullable = False, default = Status.EDITING)

    name             = Column(String, nullable = False, default = '')
    creature_type_id = Column(Integer, ForeignKey('traits_creaturetype.id'), nullable = False)
    genealogy_id     = Column(Integer, ForeignKey('traits_genealogy.id'))
    affiliation_id   = Column(Integer, ForeignKey('traits_affiliation.id'))
    subgroup_id      = Column(Integer, ForeignKey('traits_subgroup.id'))

    date_created     = Column(DateTime, nullable = False, default = datetime.utcnow)
    date_submitted   = Column(DateTime)
    date_approved    = Column(DateTime)
    date_last_edited = Column(DateTime, nullable = False, default = datetime.utcnow, onupdate = datetime.utcnow)

    def __unicode__(self):
        return self.name

    user      = relationship('User')
    chronicle = relationship('Chronicle')

    creature_type = relationship('CreatureType')
    genealogy     = relationship('Genealogy')
    affiliation   = relationship('Affiliation')
    subgroup      = relationship('Subgroup')

    attributes        = relationship('CharacterAttribute')
    skills            = relationship('CharacterSkill')
    skill_specialties = relationship('CharacterSkillSpecialty')
    powers            = relationship('CharacterPower')
    merits            = relationship('CharacterMerit')
    flaws             = relationship('CharacterFlaw')
    combat_traits     = relationship('CharacterCombatTrait')
    misc_traits       = relationship('CharacterMiscTrait')


# class XPRecord (models.Model):
#     game      = models.ForeignKey(Game)
#     character = models.ForeignKey(Character)
#     amount    = models.SmallIntegerField()
#     note      = models.CharField(max_length = 255)

#     class Meta (object):
#         ordering = ('game__date', 'character')


class CharacterTrait (AppLabel, BaseModel):
    def __repr__ (self):
        return "<{}({}, {}, {})>".format(
            type(self).__name__,
            '(un-named chronicle)' if not self.character.chronicle
                else self.character.chronicle.name,
            self.character.name,
            self.trait.name
        )

    id = Column(Integer, primary_key = True)
    trait_type = Column(String, nullable = False)

    character_id = Column(Integer, ForeignKey(Character.id),      nullable = False)
    trait_id     = Column(Integer, ForeignKey('traits_trait.id'), nullable = False)

    # TODO(Emery): Limit the value of `trait_type` to enforce using the
    #              appropriate child class when linking to the appropriate type
    #              of trait.
    # possible solution: composite foreign key using ForeignKeyConstraint
    #      e.g. ForeignKeyConstraint(
    #               (trait_id, trait_type),
    #               (Trait.id, Trait.trait_type)
    #           )
    #    (This won't work right now.  It will break skill-specialties.)

    __mapper_args__ = {
        'polymorphic_on': trait_type,
    }

    character = relationship(Character)
    trait     = relationship('Trait', lazy = 'joined')


class CharacterAttribute (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating = Column(SmallInteger, nullable = False, default = 1)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
        CheckConstraint(rating > 0, name = 'positive_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'attribute',
    }


class CharacterCharacterText (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    text = Column(Text, nullable = False, default = '')

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'character_text',
    }


class CharacterCombatTrait (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating = Column(SmallInteger)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'combat_trait',
    }


class CharacterFlaw (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating        = Column(SmallInteger)
    specification = Column(String)
    description   = Column(Text)

    __table_args__ = (
        CheckConstraint(or_(rating == None, rating > 0), name = 'positive_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'flaw',
    }


class CharacterMerit (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating        = Column(SmallInteger)
    specification = Column(String)
    description   = Column(Text)

    __table_args__ = (CheckConstraint(rating > 0, name = 'positive_rating'),)

    __mapper_args__ = {
        'polymorphic_identity': 'merit',
    }


class CharacterMiscTrait (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating      = Column(SmallInteger, nullable = False)
    description = Column(Text)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
        CheckConstraint(rating >= 0, name = 'non_negative_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'misc_trait',
    }


class CharacterPower (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'power',
    }


class CharacterSkill (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    rating = Column(SmallInteger, nullable = False, default = 0)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id),  # TODO(Emery): enforce this
        CheckConstraint(rating >= 0, name = 'non_negative_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'skill',
    }


class CharacterSkillSpecialty (CharacterTrait):
    id = Column(Integer, ForeignKey(CharacterTrait.id, ondelete = 'CASCADE'), primary_key = True)

    specialty = Column(String, nullable = False)

    __table_args__ = (
        # UniqueConstraint(character_id, trait_id, specialty),  # TODO(Emery): enforce this
    )

    __mapper_args__ = {
        'polymorphic_identity': 'skill_specialty',
    }
