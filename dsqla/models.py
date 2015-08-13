## @package dsqla.models
#  Model tools for SQLAlchemy.


from sys import _getframe

from collections import OrderedDict
from datetime import datetime, date, time
from decimal import Decimal
from enum import Enum
from json import dumps, JSONEncoder

from sqlalchemy.event import listens_for
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.schema import Column
from sqlalchemy.sql.schema import MetaData as sqla_MetaData
from sqlalchemy.types import INTEGER


## Override the default MetaData class to add some custom fields.
#
class MetaData (sqla_MetaData):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.models          = OrderedDict()
        self.models_by_table = OrderedDict()


## Base class for your base model class.
#
#  This breaks the `super()` chain of any mixins.
class BaseModelBase (object):
    @classmethod
    def __declare_first__ (cls):
        pass

    @classmethod
    def __declare_last__ (cls):
        pass


## Mixin to add the host model class to the table-model map.
#
#  NOTE: This depends on the MetaData class above.
class TableToModelMap (object):
    @classmethod
    def __declare_last__ (cls):
        super().__declare_last__()

        table = cls.__table__
        metadata = table.metadata

        metadata.models[cls.__tablename__] = cls
        metadata.models_by_table[table]    = cls


# ## Register a callback with the BaseModel to save a mapping of the Table class
# #  to the Model class.
# #
# #  NOTE: This depends on the MetaData class above.
# def generate_table_to_model_map (Base):
#     @listens_for(Base, 'instrument_class', propagate = True)
#     def on_new_class (mapper, cls_):
#         table = getattr(cls_, '__table__', None)
#         if table is None:
#             return

#         table.metadata.models[cls_.__tablename__] = cls_
#         table.metadata.models_by_table[table]     = cls_


def get_model (application, model):
    exec("from {}.models import {} as Model".format(application, model), globals())
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
            return str(obj)

        # Model
        elif isinstance(obj, ToJSON):
            return obj.to_dict()

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


## Helper function to retrieve the model on the other side of the reference.
#
#  @arg column A model/table colum that has a foreign key.
#
#  NOTE: In order to make use of this function, you must have constructed the
#        models in question using the MetaData class defined above and have
#        called `generate_table_to_model_map()` on the base model class.
def get_referenced_model (column):
    for foreign_key in column.foreign_keys: break
    table = foreign_key.column.table
    return table.metadata.models_by_table[table]


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
