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

Tools.resolve = (name, root = window) ->
    return root if not name
    return name if not _.isString name
    tokens = name.split '.'
    obj = root

    for item in tokens
        obj = obj[item]
        return obj if obj is undefined

    return obj


## Just a copy of Backbone's wrapError.
#
#  Backbone does not expose this sweet utility function so we copy it here.
Tools.wrap_error = (model, options) ->
    error = options.error
    options.error = (resp) ->
        error model, resp, options if error?
        model.trigger 'error', model, resp, options


Function::property = (property_name, desc) ->
    Object.defineProperty @prototype, property_name, desc

Function::class_property = (property_name, desc) ->
    Object.defineProperty @, property_name, desc
