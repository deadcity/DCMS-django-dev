Tools.create_namespace 'Tools'


class Tools.Enum
    constructor: () ->
        Tools.enum.apply this, arguments


Tools.enum = (name, elements, options) ->
    options = _.defaults {}, options,
        Base          : Tools.Enum
        initial_value : 1
        undef         : {}

    _force_creation_tag = new Object();

    EnumClass = Function('_force_creation_tag', "
        function #{name} (value) {
            if (value === _force_creation_tag) {
                return this;
            }

            if (value === undefined) {
                return #{name}._UNDEF;
            }

            if (value in #{name}._by_value) {
                return #{name}._by_value[value];
            }

            throw 'no element found with value = \"' + value + '\"';
        };
        return #{name};
    ")(_force_creation_tag)

    # # # # # #
    # EXTENDS #
    # # # # # #

    # This is just coffeescript's "extends" functionality.  We have to duplicate
    # it because we want the classname to be the passed value.

    parent = options.Base
    child = EnumClass

    for key of parent
        if parent.hasOwnProperty key
            child[key] = parent[value]

    ctor = () -> @constructor = child; @

    ctor.prototype = parent.prototype
    child.prototype = new ctor()
    child.__super__ = parent.prototype


    # # # # # # # # #
    # CLASS MEMBERS #
    # # # # # # # # #

    EnumClass._by_value = {}
    EnumClass._by_name = {}


    # # # # # # #
    # ELEMENTS  #
    # # # # # # #

    create_element = (raw) ->
        element = new EnumClass _force_creation_tag

        if _.isString raw
            element.name = raw

        else if _.isObject raw
            for key of raw
                element[key] = raw[key]

        return element

    EnumClass._UNDEF = create_element options.undef

    next_value = options.initial_value

    for raw in elements
        element = create_element raw

        if 'value' not of element
            element.value = next_value++
        else
            next_value = element.value + 1

        EnumClass._by_value[element.value] = element
        EnumClass._by_name[element.name] = element
        EnumClass[element.name] = element

    return EnumClass
