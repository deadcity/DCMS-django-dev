## @module trait_access.models
#  Provides models used to define access rules for traits.


from sys import stderr

from collections import defaultdict
from enum import Enum

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from DCMS.model_base import BaseModel

from characters.models import CharacterTrait
from dsqla.column_types import EnumColumn
from dsqla.models import app_label
from dsqla.session import session
from traits.models import Trait


AppLabel = app_label('trait_access')


class AccessRule (AppLabel, BaseModel):
    class Access (Enum):
        FORCE = 1
        ALLOW = 2
        DENY  = 3
        HIDE  = 4

    id = Column(Integer, primary_key = True)
    rule_type = Column(String, nullable = False)

    # A rule is associated with a particular Chronicle or ChronicleTemplate.
    # This may differ from the chronicle of the trait this rule references.
    chronicle_id = Column(Integer, ForeignKey('chronicles_chroniclebase.id'), nullable = False)
    trait_id     = Column(Integer, ForeignKey('traits_trait.id'),             nullable = False)

    priority = Column(Integer, nullable = False)
    access   = Column(EnumColumn(Access, name = 'access_rule_access'), nullable = False)

    __mapper_args__ = {
        'polymorphic_on': rule_type,
    }

    chronicle = relationship('ChronicleBase')
    trait     = relationship('Trait')

    def evaluate (self, character):
        raise NotImplementedError("This method must be overriden by a child class.")


def evaluate_trait (character, trait):
    for access_rule in session.query(AccessRule).filter(
        AccessRule.trait == trait,
        AccessRule.chronicle_id.in_(c.id for c in character.chronicle.all_chronicles)
    ).order_by(AccessRule.priority.asc()):
        result = access_rule.evaluate(character)
        if result:
            return result

    stderr.write("ERROR: Trait \"{}\" has no default-access rule.\n".format(trait))


def calculate_availabilities (character, trait_list):
    availabilities = defaultdict(lambda: defaultdict(list))
    for trait in trait_list:
        access = evaluate_trait(character, trait)
        if access is AccessRule.Access.DENY:
            inheritance_source = character.chronicle.inheritance_source(trait)
            if getattr(inheritance_source, 'hide_denied_traits', False):
                access = AccessRule.Access.HIDE

        if access is not None:
            availabilities[type(trait).__name__][access.name].append(trait)

    return availabilities


class DefaultAccess (AccessRule):
    id = Column(Integer, ForeignKey(AccessRule.id, ondelete = 'CASCADE'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'default_access',
    }

    def evaluate (self, character):
        return self.access


class CharacterIs (AccessRule):
    id = Column(Integer, ForeignKey(AccessRule.id, ondelete = 'CASCADE'), primary_key = True)

    character_id = Column(Integer, ForeignKey('characters_character.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'character_is',
    }

    character = relationship('Character')

    def evaluate (self, character):
        if self.character is character:
            return self.access


class CharacterIsNot (AccessRule):
    id = Column(Integer, ForeignKey(AccessRule.id, ondelete = 'CASCADE'), primary_key = True)

    character_id = Column(Integer, ForeignKey('characters_character.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'character_is_not',
    }

    character = relationship('Character')

    def evaluate (self, character):
        if self.character is not character:
            return self.access


class CharacterHasTrait (AccessRule):
    id = Column(Integer, ForeignKey(AccessRule.id, ondelete = 'CASCADE'), primary_key = True)

    other_trait_id = Column(Integer, ForeignKey('traits_trait.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'character_has_trait',
    }

    other_trait = relationship('Trait', foreign_keys = other_trait_id)

    def evaluate (self, character):
        other_trait_type = self.other_trait.trait_type
        if other_trait_type in (
            'creature_type',
            'genealogy',
            'affiliation',
            'subgroup',
        ):
            if getattr(character, other_trait_type) is self.other_trait:
                return self.access

        else:
            query = session.query(CharacterTrait).filter(
                CharacterTrait.character  == character,
                CharacterTrait.trait      == self.other_trait,
                CharacterTrait.trait_type != 'skill_specialty'
            )
            if len(query.all()) > 0:
                return self.access


class CharacterDoesNotHaveTrait (AccessRule):
    id = Column(Integer, ForeignKey(AccessRule.id, ondelete = 'CASCADE'), primary_key = True)

    other_trait_id = Column(Integer, ForeignKey('traits_trait.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'character_does_not_have_trait',
    }

    other_trait = relationship('Trait', foreign_keys = other_trait_id)

    def evaluate (self, character):
        other_trait_type = self.other_trait.trait_type
        if other_trait_type in (
            'creature_type',
            'genealogy',
            'affiliation',
            'subgroup',
        ):
            if getattr(character, other_trait_type) is not self.other_trait:
                return self.access

        else:
            query = session.query(CharacterTrait).filter(
                CharacterTrait.character  == character,
                CharacterTrait.trait      == self.other_trait,
                CharacterTrait.trait_type != 'skill_specialty'
            )
            if len(query) == 0:
                return self.access
