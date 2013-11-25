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


Tools.mixin = (Base, mixins...) ->
    class Mixed extends Base

    for Mixin in mixins by -1  # earlier mixins override later ones
        # Class members.
        for name, member of Mixin
            Mixed[name] = member

        # Prototype members.
        for name, member of Mixin::
            Mixed::[name] = member

    Mixed
