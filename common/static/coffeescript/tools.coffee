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


Function::define_property = (property_name, desc) ->
    Object.defineProperty @prototype, property_name desc
