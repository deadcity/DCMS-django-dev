from itertools import product


class Element (object):
    def __init__ (self, name, **kwargs):
        self.__name = name

        for key, value in kwargs.items():
            setattr(self, '__' + key, value)

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
        new_class = super(_Enum_Metaclass, mtcls).__new__(mtcls, name, bases, ext_attrs)
        Elem = type(name + '_Element', (Element,), { '_enum': new_class })
        setattr(new_class, '_Element', Elem)

        for name, fields in attrs.items():
            if name.startswith('__') and name.endswith('__'):
                continue

            if not type(fields) is dict:
                fields = { 'value': fields }

            # Create enum element.
            elem = Elem(name, **fields)
            elements.append(elem)
            setattr(new_class, name, elem)

            # Identify enum element in each index.
            make_elem_prop = lambda key: property(lambda self: getattr(self, '__' + key))
            make_enum_from = lambda key: classmethod(lambda cls, value: cls._indeces[key][value])
            for key, value in fields.items():
                if key in indeces:
                    index = indeces[key]
                else:
                    index = indeces[key] = {}
                    setattr(Elem,      key,           make_elem_prop(key))
                    setattr(new_class, 'from_' + key, make_enum_from(key))
                index[value] = elem

        for elem, field in product(elements, indeces.keys()):
            if not hasattr(elem, '__' + field):
                setattr(elem, '__' + field, None)

        return new_class

    @property
    def all (cls):
        return cls._elements


class Enum (object):
    __metaclass__ = _Enum_Metaclass
