## @module traits.models
#  Provides models related to traits.


from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import CheckConstraint, Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql.expression import or_
from sqlalchemy.types import Boolean, Integer, String

from DCMS.model_base import BaseModel

from dsqla.models import app_label


AppLabel = app_label('traits')


class TraitType (AppLabel, BaseModel):
    __abstract__ = True

    def __repr__ (self):
        return "<{}({})>".format(type(self).__name__, self.name)

    def __str__ (self):
        return self.name

    def __unicode__ (self):
        return unicode(str(self))

    id = Column(Integer, primary_key = True)

    name  = Column(String, unique = True, nullable = False)
    label = Column(String, nullable = False, default = '')


class AttributeType   (TraitType): pass
class FlawType        (TraitType): pass
class MeritType       (TraitType): pass
class SkillType       (TraitType): pass


class Trait (AppLabel, BaseModel):
    def __repr__ (self):
        return "<{}({})>".format(type(self).__name__, self.name)

    id = Column(Integer, primary_key = True)
    _discriminator = Column(String, nullable = False)

    name  = Column(String, unique = True, nullable = False)
    label = Column(String, nullable = False, default = '')

    __mapper_args__ = {
        'polymorphic_on': _discriminator,
    }


class Affiliation (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'affiliation',
    }


class Attribute (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    attribute_type_id = Column(Integer, ForeignKey(AttributeType.id))
    order             = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'attribute',
    }

    attribute_type = relationship(AttributeType)


class CharacterText (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    hide_from_player = Column(Boolean, nullable = False, default = False)
    include_on_sheet = Column(Boolean, nullable = False, default = False)

    __mapper_args__ = {
        'polymorphic_identity': 'character_text',
    }


class CombatTrait (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    order = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'combat_trait',
    }


class CreatureType (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    genealogy_name   = Column(String)
    affiliation_name = Column(String)
    subgroup_name    = Column(String)
    power_name       = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'creature_type',
    }


class Flaw (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    flaw_type_id = Column(Integer, ForeignKey(FlawType.id))
    requires_specification = Column(Boolean, nullable = False, default = False)
    requires_description = Column(Boolean, nullable = False, default = False)

    __mapper_args__ = {
        'polymorphic_identity': 'flaw',
    }

    flaw_type = relationship(FlawType)


class Genealogy (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'genealogy',
    }


class Merit (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    merit_type_id = Column(Integer, ForeignKey(MeritType.id))
    requires_specification = Column(Boolean, nullable = False, default = False)
    requires_description = Column(Boolean, nullable = False, default = False)

    __mapper_args__ = {
        'polymorphic_identity': 'merit',
    }

    merit_type = relationship(MeritType)


class AllowedMeritRating (AppLabel, BaseModel):
    merit_id = Column(Integer, ForeignKey(Merit.id))
    rating = Column(Integer, nullable = False)

    __table_args__ = (
        PrimaryKeyConstraint(merit_id, rating),
        CheckConstraint(rating >= 0, name = 'non_negative_rating'),
    )

    merit = relationship(Merit, backref = backref('allowed_ratings'))


class MiscTrait (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    requires_description = Column(Boolean, nullable = False, default = False)

    __mapper_args__ = {
        'polymorphic_identity': 'misc_trait',
    }


class PowerGroup (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'power_group',
    }


class Power (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    rating = Column(Integer)
    power_group_id = Column(Integer, ForeignKey(PowerGroup.id))

    __table_args__ = (
        CheckConstraint(or_(rating == None, rating > 0), name = 'positive_rating'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'power',
    }

    power_group = relationship(PowerGroup, foreign_keys = (power_group_id,))


class Skill (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    skill_type_id = Column(Integer, ForeignKey(SkillType.id))

    __mapper_args__ = {
        'polymorphic_identity': 'skill',
    }

    skill_type = relationship(SkillType)


class Subgroup (Trait):
    id = Column(Integer, ForeignKey(Trait.id, ondelete = 'CASCADE'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'subgroup',
    }
