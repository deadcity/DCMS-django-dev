create_namespace = (namespace_name) ->
    if not namespace_name then return window
    tokens = namespace_name.split '.'
    parent = window

    for name in tokens
        parent[name] = parent[name] ? {}
        parent = parent[name]

    return parent

Tools = create_namespace 'Tools'
Tools.create_namespace = create_namespace


## Just a copy of Backbone's wrapError.
#
#  Backbone does not expose this sweet utility function so we copy it here.
Tools.wrap_error = (model, options) ->
    error = options.error
    options.error = (resp) ->
        error model, resp, options if error?
        model.trigger 'error', model, resp, options


Function::define_property = (property_name, desc) ->
    Object.defineProperty @prototype, property_name, desc
