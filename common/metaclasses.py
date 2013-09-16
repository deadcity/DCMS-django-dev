from collections import OrderedDict

from django.db import models


class Model_Metaclass(models.base.ModelBase):
    def __new__(metaclass, name, bases, attrs):
        fields = OrderedDict()

        for base in bases:
            if hasattr(base, 'fields'):
                fields.update(getattr(base, 'fields'))

        for key, val in attrs.items():
            if isinstance(val, models.fields.Field):
                fields[key] = val

        return super(Model_Metaclass, metaclass).__new__(
            metaclass, name, bases, dict(fields = fields, **attrs)
        )
