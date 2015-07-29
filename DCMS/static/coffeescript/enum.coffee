###
    @file  enum.coffee
    @brief Base class and factory function for providing strongly-typed
        Enumerations in coffeescript.

    @dependencies
        tools.coffee

    The following two code blocks are equivalent. The factory function format:

        Color = Tools.enum 'Color', [
            'RED'
            'GREEN'
            'BLUE'
        ]

    ... and the meta-class format:

        Color = new Tools.Enum 'Color', [
            'RED'
            'GREEN'
            'BLUE'
        ]

    The first, using the factory function, is the prefered syntax. They both
    generate several things, first of which is a new class called "Color" which
    inherits from `Tools.Enum`. This is the "Enumeration class". Elements of the
    Enumeration will be instances of this class. Every enum element will have
    two member variables: "name" and "value".

    "value" by default is an incrementing integer starting from 1. "name" is a
    string identifying that element ("RED", "GREEN", or "BLUE"). Each element is
    accessible as a member of the Enumeration class under this name. (ie:
    Color.BLUE)

        Color.BLUE.name   # "BLUE"
        Color.BLUE.value  # 3

    For iterating over the elements of the Enumeration, the Enumeration class
    has a member called "_elements" that is simply an array of the elements in
    the order they were defined.

        for color in Color._elements
            console.log color.name

    Elements (instances of the Enumeration class) can only be instantiated when
    the Enumeration class is originally created. Any call of `new Color()` will
    not result in the creation of a new element. This is instead used as a way
    to lookup the element by value.

    An element can fetched based on its value using parentheses, or by name
    using square brackets. In short, the following are all equivalent ways of
    accessing the <GREEN> element of the Color enum:

        Color.GREEN
        Color['GREEN']
        Color(2)
        new Color(2)  # This one works, but you shouldn't do it this way.

    You can customize the structure of an element by providing an object instead
    of a string when specifying that element. The object's properties will then
    be shallow-copied into the resultant element. If "value" is not specified,
    it will be set to the previous element's value + 1. There is no "name"
    property automatically included. You must specify "name" explicitly if you
    want that element to be accessible as a member of the Enumeration class.

        Color = Tools.enum 'Color', [
            { 'name': 'RED',   hex: '#FF0000', 'color_name': 'red'   }
            { 'name': 'GREEN', hex: '#00FF00', 'color_name': 'green' }
            { 'name': 'BLUE',  hex: '#0000FF', 'color_name': 'blue'  }
            'ALPHA'
            {                  hex: '#FA8072', 'color_name': 'salmon' }
        ]

        Color.RED.hex                  # '#FF0000'
        Color.ALPHA.value              # 4
        Color.salmon                   # <undefined>
        Color._elements[2].name        # 'BLUE'
        Color._elements[4].name        # <undefined>
        Color._elements[4].color_name  # 'salmon'

    Every enumeration will also generate an element corresponding to
    `undefined`. By default, this will be an empty object as an instance of the
    enumeration class, but it can be customized through an item of the `options`
    argument to the factory function following the same rules as element
    customization above. (See the documentation for the factory function below.)
    This element will not be part of the `Enumeration._elements` array but is
    instead accessible as Enumeration._UNDEF and is returned from the
    constructor if you do not pass any arguments.

        Color._UNDEF
        Color()
        Color(undefined)
###


Tools.create_namespace 'Tools'


###
    A default base class to use for Enumerations. When creating a new enum, you
    should simply use the factory function defined below.
###
class Tools.Enum
    constructor: () ->
        Tools.enum.apply this, arguments


###
    A factory function for creating new Enumerations.

    @arg name A string to use as the name of the Enumeration class.
    @arg elements An array of strings used to generate the elements of the
        Enumeration. The resultant elements will be objects with two members: a
        'name' which is simply the string corresponding to that element, and a
        'value' which is an auto-incremented integer. Alternatively, elements of
        the `elements` array can be objects. If so, then resultant instances of
        the Enumeration will copy the members of the corresponding object. If
        'value' is not specified in an object, it will be implicitly generated.
        If 'value' is specified, the 'value' member of subsequent elements will
        be continued from the specified value.
    @arg options Configuration for the Enumeration.
        @option Base (optional; default `Tools.Enum`) A base class to use for
            the Enumeration.
        @option initial_value (optional; default 1) The initial value to use as
            the 'value' member of each element, assuming it isn't specified in
            `elements`.
        @option undef (optional; default `{}`) The factory will generate an
            instance of the Enumeration with no 'value' specified to be used to
            represent `undefined`. This parameter will be used to generate that
            element in the exact same manner as those specified in the
            `elements` argument (except for the missing "value" member). If you
            do not specify a string here, the "UNDEF" element will have no
            "name" member. This "UNDEF" element will be available as a class-
            variable of the Enumeration class called "_UNDEF".
###
Tools.enum = (name, elements, options) ->
    options = _.defaults {}, options,
        Base          : Tools.Enum
        initial_value : 1
        undef         : {}

    # This tag will be used to allow the creation of new Enumeration elements
    # only in the context of this execution of this factory function. The
    # constructor we create below will only create new objects if it is passed
    # this tag. So once this tag falls out of scope, it will no longer exist
    # (outside of the constructor's closure) thus locking up that code
    # path of the constructor forever.
    _force_creation_tag = new Object();

    # Dynamically create the constructor so that the constructor's name is
    # correctly specified.
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

    # This is just coffeescript's "extends" functionality. We have to duplicate
    # it because we want some customization. Namely, we want the classname to be
    # the passed value.

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

    EnumClass._elements = []
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
            _.extend element, raw

        return element

    EnumClass._UNDEF = create_element options.undef

    next_value = options.initial_value

    for raw in elements
        element = create_element raw

        if 'value' not of element
            element.value = next_value++
        else
            next_value = element.value + 1

        EnumClass._elements.push element

        EnumClass._by_value[element.value] = element
        if element.name?
            EnumClass._by_name[element.name] = element
            EnumClass[element.name] = element

    return EnumClass
