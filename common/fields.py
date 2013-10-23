from django.core import exceptions, validators
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

    def __init__ (self, enum, db_type = 'VARCHAR', **kwargs):
        self.enum = enum
        self._db_type = db_type
        choices = [(elem.value, elem) for elem in enum._elements]
        super(EnumField, self).__init__(choices = choices, **kwargs)

    def _validate_enum (self, value):
        if not (value in self.enum._elements):
            msg = self.error_messages['invalid'] % (value, str(self.enum))
            raise exceptions.ValidationError(msg)

    def db_type (self, connection):
        return self._db_type

    def to_python (self, value):
        # print '++ to_python(value)'
        # print "  | value = {} '{}'".format(type(value), value)
        # print type(value), type
        if value is None or str(value) is '':
            return None

        if isinstance(value, Element) and value in self.enum._elements:
            return value

        try:
            return self.enum.from_value(int(value))

        except KeyError:
            # print type(value), value
            msg = self.error_messages['invalid'] % (value, str(self.enum))
            raise exceptions.ValidationError(msg)

    def validate(self, value, model_instance):
        """
        Validates value and throws ValidationError.
        """
        # print '++ validate(value, model_instance)'
        # print "  | value = {} '{}'".format(type(value), value)
        # print "  | model = {} '{}'".format(type(model_instance), model_instance)

        if not self.editable:
            # Skip validation for non-editable fields.
            return

        # print '++ validate(value, model_instance)'
        # print "  | value = {} '{}'".format(type(value), value)

        if self._choices and value not in validators.EMPTY_VALUES:
            for opt_key, opt_value in self.choices:
                # print "  | '{}' : {} '{}'".format(opt_key, type(opt_value), opt_value)
                if value == opt_value:
                    return

            msg = self.error_message=['invalid_choice'] % str(value)
            raise exceptions.ValidationError(msg)

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_message['null'])

        if not self.blank and value in validators.EMPTY_VALUES:
            raise exceptions.ValidationError(self.error_messages['blank'])

        # return super(EnumField, self).validate(value, model_instance)

    def get_prep_value (self, value):
        if value is None:
            return None

        self._validate_enum(value)
        return value.value
