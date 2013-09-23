from inspect import isclass


class Element (object):
    def __init__ (self, enum, name, label = None, value = None):
        self.__enum  = enum
        self.__name  = name
        self.__label = label
        self.__value = value

    @property
    def name (self):
        return self.__name

    @property
    def label (self):
        return self.__label if self.__label else self.__name

    @property
    def value (self):
        return self.__value

    def __str__ (self):
        return self.label

    def __repr__ (self):
        return '<{}: {}>'.format(self.__enum._name, self.name)

    def __unicode__ (self):
        return str(self)


class _Enum_Metaclass (type):
    def __new__ (mtcls, name, bases, attrs):
        elements = []
        elem_by_name  = {}
        elem_by_label = {}
        elem_by_value = {}
        new_class = super(_Enum_Metaclass, mtcls).__new__(mtcls, name, bases, {
            '_name'     : name,
            '_elements' : elements,
            '_by_name'  : elem_by_name,
            '_by_label' : elem_by_label,
            '_by_value' : elem_by_value
        })

        for key, item in attrs.items():
            if key.startswith('_'): continue
            if isclass(item): continue

            if type(item) is dict:
                elem = Element(new_class, key, **item)
            else:
                elem = Element(new_class, key, value = item)
            setattr(new_class, key, elem)
            elements.append(elem)
            elem_by_name  [elem.name]  = elem
            elem_by_label [elem.label] = elem
            elem_by_value [elem.value] = elem

        return new_class

    def __str__ (cls):
        return "<enum '{}'>".format(cls._name)

    def from_label (cls, label):
        return cls._by_label[label]

    def from_value (cls, value):
        return cls._by_value[value]


class Enum (object):
    __metaclass__ = _Enum_Metaclass


class Field (Enum):
    NAME  = { 'value': 0, 'label': 'name'  }
    LABEL = { 'value': 1, 'label': 'label' }
    VALUE = { 'value': 2, 'label': 'value' }
setattr(Enum, 'Field', Field)
