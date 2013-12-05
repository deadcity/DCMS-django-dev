from collections import OrderedDict

from django.db import DatabaseError, models


class HistoryBackedManager(models.Manager):
    def __init__(self, date_field, *args, **kwargs):
        super(HistoryBackedManager, self).__init__(*args, **kwargs)
        self._date_field = date_field

    def get_deleted(self, date, **kwargs):
        fields = [(self._date_field, date)] + kwargs.items()
        return self.raw(
            'SELECT * FROM "{}" WHERE {}'.format(
                self.model._meta.db_table + '_deleted',
                ' AND '.join(field + ' = %s' for field, value in fields)
            ),
            [value for field, value in fields]
        )


class Model_Metaclass(models.base.ModelBase):
    def __new__(mtcls, name, bases, attrs):
        fields = OrderedDict()

        for base in bases:
            if hasattr(base, 'fields'):
                fields.update(getattr(base, 'fields'))

        for key, val in attrs.items():
            if isinstance(val, models.fields.Field):
                fields[key] = val

        return super(Model_Metaclass, mtcls).__new__(
            mtcls, name, bases, dict(fields = fields, **attrs)
        )


class ReadOnly(object):
  def save(self, *args, **kwargs):
    raise DatabaseError(self._meta.object_name + " is a read-only model.")

  def delete(self, *args, **kwargs):
    raise DatabaseError(self._meta.object_name + " is a read-only model.")
