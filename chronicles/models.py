## @module chronicls.models
#  Provides models for the `chronicles` application.


from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column, ForeignKey, Table, UniqueConstraint
from sqlalchemy.types import Boolean, Date, Integer, String, Text

from DCMS.model_base import BaseModel

from auth.models import User
from dsqla.models import app_label


AppLabel = app_label('chronicles')


class ChronicleBase (AppLabel, BaseModel):
    def __repr__ (self):
        return "<{}({})>".format(type(self).__name__, self.name)

    id = Column(Integer, primary_key = True)
    _discriminator = Column(String, nullable = False)

    enabled     = Column(Boolean, nullable = False, default = True)
    name        = Column(String, nullable = False, default = '', unique = True)
    description = Column(Text, nullable = False, default = '')

    __mapper_args__ = {
        'polymorphic_on': _discriminator,
    }


class ChronicleTemplate (ChronicleBase):
    id = Column(Integer, ForeignKey(ChronicleBase.id, ondelete = 'CASCADE'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'cronicle_template',
    }


class Chronicle (ChronicleBase):
    id = Column(Integer, ForeignKey(ChronicleBase.id, ondelete = 'CASCADE'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'chronicle',
    }

    templates = relationship('ChronicleInheritsTemplate')
    games = relationship('Game')


class ChronicleInheritsTemplate (AppLabel, BaseModel):
    chronicle_id          = Column(Integer, ForeignKey(Chronicle.id),         primary_key = True)
    chronicle_template_id = Column(Integer, ForeignKey(ChronicleTemplate.id), primary_key = True)

    # When access to a trait from this chronicle-template is denied, hide the trait.
    hide_denied_traits = Column(Boolean, nullable = False, default = False)

    chronicle = relationship(Chronicle)
    template = relationship(ChronicleTemplate)


class Game (AppLabel, BaseModel):
    def __repr__ (self):
        return "<Game({}, {})>".format(self.chronicle.name, self.name)

    id = Column(Integer, primary_key = True)

    enabled = Column(Boolean, nullable = False, default = True)

    name         = Column(String, nullable = False)
    chronicle_id = Column(Integer, ForeignKey(Chronicle.id), nullable = False)
    date         = Column(Date)

    __table_args__ = (
        UniqueConstraint(chronicle_id, name),
    )

    chronicle = relationship(Chronicle)
