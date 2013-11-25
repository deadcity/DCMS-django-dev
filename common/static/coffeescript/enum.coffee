Tools.create_namespace 'Tools'


class EnumElement
    constructor: (pairs...) ->
        @[key] = value for [key, value] in pairs

    valueOf: () ->
        @value

    toString: () ->
        @name

    toJSON: () ->
        attrs = {}
        _.each _.keys(@), (key) ->
            attrs[key] = @[key]
        , @
        attrs


class Tools.Enum
    constructor: (elements) ->
        cur_val = -1
        @_elements = []
        for el in elements
            if el.id? and not el.value?
                el.value = el.id
            cur_val = el.value ? ++cur_val
            el = _.extend _.clone(el), {value: cur_val}
            @_elements.push new EnumElement _.pairs(el)...

        @[el.name] = el for el in @_elements
        @_by_value = {}
        @_by_value[el.value] = el for el in @_elements

    get: (value) ->
        if value in @_elements then return value
        if value in _.pluck @_elements, 'name' then return @[value]
        return @_by_value[value] ? @_by_value[value]
