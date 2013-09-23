from django.core import exceptions
from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from common.enum import Element, Enum


class EnumField (models.Field):
    """
    A field class that maps from an Enum type.
    """

    __metaclass__ = models.SubfieldBase

    default_error_messages = {
        'invalid_enum_config': _("'%s' is not a valid value for '%s'"),
        'invalid': _("'%s' - value must be an enum value of '%s'"),
    }

    def __init__ (self, enum, store_method = Enum.Field.VALUE, db_type = 'VARCHAR', **kwargs):
        self.enum = enum
        self.store_method = store_method
        self._db_type = db_type
        super(EnumField, self).__init__(**kwargs)

        if not (store_method in Enum.Field._elements):
            msg = self.error_messages['invalid_enum_config'] % (store_method, 'store_method')
            raise exceptions.FieldError(msg)

    def _validate_enum (self, value):
        if not (value in self.enum._elements):
            msg = self.error_messages['invalid'] % (value, str(self.enum))
            raise exceptions.ValidationError(msg)

    def db_type (self, connection):
        return self._db_type

    def to_python (self, value):
        print type(value), type
        if value is None or str(value) is '':
            return None

        if isinstance(value, Element) and value in self.enum._elements:
            return value

        try:
            if self.store_method is Enum.Field.NAME:
                return self.enum._by_name[value]

            elif self.store_method is Enum.Field.LABEL:
                return self.enum._by_label[value]

            elif self.store_method is Enum.Field.VALUE:
                return self.enum._by_value[value]

        except KeyError:
            print type(value), value
            msg = self.error_messages['invalid'] % (value, str(self.enum))
            raise exceptions.ValidationError(msg)

    def get_prep_value (self, value):
        if value is None:
            return None

        self._validate_enum(value)

        if self.store_method is Enum.Field.NAME:
            return value.name

        elif self.store_method is Enum.Field.LABEL:
            return value.label

        elif self.store_method is Enum.Field.VALUE:
            return value.value
