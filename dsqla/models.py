## @package dsqla.models
#  Model tools for SQLAlchemy.


from sys import _getframe

from datetime import datetime, date, time
from decimal import Decimal
from enum import Enum
from json import dumps, JSONEncoder

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.schema import Column
from sqlalchemy.types import INTEGER


def get_model (application, model):
    exec("from {}.models import {} as Model".format(application, model))
    return Model


class ModelEncoder (JSONEncoder):
    def default (self, obj):
        # Enum
        if isinstance(obj, Enum):
            return obj.name

        # Decimal
        elif isinstance(obj, Decimal):
            return float(obj)

        # datetime, date, or time
        elif isinstance(obj, (datetime, date, time)):
            return unicode(obj)

        # (others)
        else:
            return super(ModelEncoder, self).default(obj)


## Generate a mixin that specifies an _app_label.
#
def app_label (app_name):
    module_name = _getframe(1).f_globals.get('__name__', '__main__')
    app_label_mixin = type(
        'AppLabel',
        (object,),
        { '_app_label': app_name, }
    )
    app_label_mixin.__module__ = module_name
    return app_label_mixin


## Mixin to generate the database table name as <application_name>_<model_name>.
#
class DjangoTablename (object):
    @declared_attr
    def __tablename__ (cls):
        app_label = getattr(cls, '_app_label', None)
        model_name = cls.__name__.lower()
        if app_label is None:
            return model_name
        else:
            return "{}_{}".format(app_label, model_name)


## Mixin to add an integer ID column to the front of the table.
#
class IdColumn (object):
    id = Column(INTEGER, primary_key = True)


## Mixin to add JSON serialization functionality.
#
class ToJSON (object):
    def to_dict (self):
        return {
            column_name: getattr(self, column_name, None)
            for column_name in self.__mapper__.columns.keys()
        }

    def to_json (self):
        return dumps(self.to_dict(), cls = ModelEncoder)
