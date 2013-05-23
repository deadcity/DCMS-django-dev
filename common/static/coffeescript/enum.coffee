Enum_NS = Tools.create_namespace 'Enum'


class Enum_NS.Element
    constructor: (pairs...) ->
        @[key] = value for [key, value] in pairs

    valueOf: () ->
        @value

    toString: () ->
        @name


class Enum_NS.Enum
    constructor: (elements) ->
        cur_val = -1
        @_elements = []
        for el in elements
            cur_val = el.value ? ++cur_val
            el = _.extend _.clone(el), {value: cur_val}
            @_elements.push new Enum_NS.Element _.pairs el

        this[el.name] = el for el in @_elements
        @_by_value = {}
        @_by_value[el.value] = el for el in @_elements

    get: (value) ->
        if value in @_elements then return value
        return @_by_value[value] ? @[value]
