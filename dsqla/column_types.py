## @package dsqla.column_types


from sqlalchemy import types


## A SQLAlchemy column type for values that are Enums.
#
#  This column type functions almost exactly like SQLAlchemy's Enum column type
#  except that, in Python, it operates with a strongly defined Enumeration type.
class EnumColumn (types.TypeDecorator, types.SchemaType):
    def __init__ (self, Enum, *args, **kwargs):
        self._Enum = Enum
        names = tuple(member.name for member in Enum)
        if 'inherit_schema' not in kwargs:
            kwargs['inherit_schema'] = True
        types.TypeDecorator.__init__(self, *(names + args), **kwargs)
        types.SchemaType.__init__(self, *args, **kwargs)

    @property
    def Enum (self):
        return self._Enum

    impl = types.Enum

    def process_bind_param (self, value, dialect):
        if value is None:
            return None
        return value.name

    def process_result_value (self, value, dialect):
        if value is None:
            return None
        return self.Enum[value]

    def _set_table (self, *args, **kwargs):
        return self.impl._set_table(*args, **kwargs)

    def adapt (self, *args, **kwargs):
        return self.impl.adapt(*args, **kwargs)
