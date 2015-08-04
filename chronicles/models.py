## @module chronicls.models
#  Provides models for the `chronicles` application.


from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column, ForeignKey, Table, UniqueConstraint
from sqlalchemy.types import Boolean, Date, Integer, String, Text

from DCMS.model_base import BaseModel
from DCMS.sequence_tools import find

from dsqla.models import app_label


AppLabel = app_label('chronicles')


class ChronicleBase (AppLabel, BaseModel):
    def __repr__ (self):
        return "<{}({})>".format(type(self).__name__, self.name)

    id = Column(Integer, primary_key = True)
    chronicle_type = Column(String, nullable = False)

    enabled     = Column(Boolean, nullable = False, default = True)
    name        = Column(String, nullable = False, default = '', unique = True)
    description = Column(Text, nullable = False, default = '')

    __mapper_args__ = {
        'polymorphic_on': chronicle_type,
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

    @property
    def all_chronicles (self):
        return set([self] + [inherits.template for inherits in self.templates])

    ## Finds the inheritance model that links this chronicle with this trait.
    #
    #  @arg trait The trait to compare
    #
    #  If `trait` comes from this chronicle itself, this function will return
    #  `self`. If `trait` comes from a chronicle-template that this chronicle
    #  inherits from, this function will return the instance of
    #  `ChronicleInheritsTemplate` that links those two chronicles. Otherwise,
    #  this function returns <None>.
    def inheritance_source (self, trait):
        source_chronicle = trait.chronicle
        if source_chronicle is self:
            return self
        return find(
            lambda model: model.chronicle is source_chronicle,
            self.templates
        )


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
