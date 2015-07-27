###
    @file  tools.coffee
    @brief A few common tools.
###


###
    A simple factory function for recursively creating nested objects.

    @arg namespace_name A string to specify the generated object path.

    @returns The last object in the namespace sequence.

    The generated nested objects are intended to be used as nested namespaces
    based on the dot-delimited specified name. Pre-existing objects that match
    the names will be used with new ones created if they don't exist. <window>
    will always be the root object.
###
create_namespace = (namespace_name) ->
    return window if not namespace_name
    tokens = namespace_name.split '.'
    parent = window

    for name in tokens
        parent[name] = parent[name] ? {}
        parent = parent[name]

    return parent

Tools = create_namespace 'Tools'
Tools.create_namespace = create_namespace


###
    Resolves a given string as an object path.

    @arg name A string of the object path to resolve. If a non-string is passed
        here, it is simply returned.
    @arg root (default: window) The root object to start searching from.

    @returns
        If `name` is falsy, returns `root`.
        If `name` is not a String, returns `name`.
        If `name` cannot be found under `root`, returns <undefined>.
        Else, returns the object referenced by `name` in `root`.
###
Tools.resolve = (name, root = window) ->
    return root if not name
    return name if not _.isString name
    tokens = name.split '.'
    obj = root

    for item in tokens
        obj = obj[item]
        return obj if obj is undefined

    return obj


###
    Just a copy of Backbone's wrapError.

    Backbone does not expose this sweet utility function so we copy it here. All
    this does is trigger the 'error' event on the model when an error occurs in
    addition to calling the normal error handler.
###
Tools.wrap_error = (model, options) ->
    error = options.error
    options.error = (resp) ->
        error model, resp, options if error?
        model.trigger 'error', model, resp, options


###
    Expose `Object.defineProperty` as a member of `Function`'s prototype to
    enable the following syntactic sugar for defining properties on classes:

        class Rectangle
            constructor: (@width, @height) ->

            @property 'area',
                get: -> @width * @height

        rect = mew Rectangle 7, 5
        rect.area  # 35

    One can also use this in defining class-methods that serve as factory
    functions for adding properties to the class or a child class. See
    'backbone-relations.coffee' for examples.
###
Function::property = (property_name, desc) ->
    Object.defineProperty @prototype, property_name, desc


###
    Similar to `property` as above except this function defines the property on
    the class itself.

        class Person
            @_instance_count = 0

            @class_property 'instance_count',
                get: @_instance_count

            constructor: ->
                @constructor._instance_count += 1

        s = [new Person(), new Person()]
        Person.instance_count  # 2

    Use this with caution when making use of Coffeescript's extends pattern as
    class-members are coppied by value to the child class. In other words, the
    current value of the property, rather than the property descriptor itself,
    will be copied.
###
Function::class_property = (property_name, desc) ->
    Object.defineProperty @, property_name, desc
