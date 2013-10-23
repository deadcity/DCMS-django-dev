from itertools import product


def make_getter    (key): return property(lambda self: getattr(self, '__' + key))
def make_enum_from (key): return classmethod(lambda cls, value: cls._indeces[key][value])


class Element (object):
    def __init__ (self, name, **kwargs):
        self.__name = name

        for key, value in kwargs.items():
            setattr(self, '__' + key, value)
            setattr(self, key, make_getter(key))

    @property
    def name (self):
        return self.__name

    def __str__ (self):
        return self.name

    def __repr__ (self):
        return '<{}: {}>'.format(self._enum._name, self.name)

    def __unicode__ (self):
        return unicode(self.name)


class _Enum_Metaclass (type):
    def __new__ (mtcls, name, bases, attrs):
        elements = []
        indeces = {}

        ext_attrs = dict(attrs.items() + [
            ('_name',     name),
            ('_elements', elements),
            ('_indeces',  indeces)
        ])

        raw_elems = {}
        for name, fields in attrs.items():
            if name.startswith('__') and name.endswith('__'):
                continue

            if not type(fields) is dict:
                fields = { 'value: fields' }

            raw_elems[name] = fields

            # Identify enum element in each index.
            ext_attrs[name] = make_getter(name)
            for key, value in fields.items():
                if not key in indeces:
                    ext_attrs['from_' + key] = make_enum_from(key)
                    for n,f in raw_elems.items():
                        if not key in f:
                            f[key] = None

        # Make Enumeration and Element classes.
        new_class = super(_Enum_Metaclass, mtcls).__new__(mtcls, name, bases, ext_attrs)
        Elem = type(name + '_Element', (Element,), { '_enum': new_class })

        for name, fields in raw_elems.items():
            # Create enum element.
            elem = Elem(name, **fields)
            elements.append(elem)
            setattr(new_class, name, elem)

            for key, value in fields.items():
                if key in indeces:
                    index = indeces[key]
                else:
                    index = {}
                    indeces[key] = index
                if value:
                    index[value] = elem

        return new_class

    @property
    def all (cls):
        return cls._elements


class Enum (object):
    __metaclass__ = _Enum_Metaclass
