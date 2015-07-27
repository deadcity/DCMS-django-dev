###
    @file  collections.coffee
    @brief A few subclasses of `Backbone.Collection` that provide commonly used
        functionality.

    @dependencies
        underscore-1.8.3.js
        backbone-1.1.2.js
###


Collections = Tools.create_namespace 'Tools.Collections'


###
    A collection that does not allow anybody to modify the models it contains.
    (However, it cannot enforce that the models themselves are read-only.)
###
class Collections.ReadOnly extends Backbone.Collection
    sync    : -> throw "This collection does not support this method."
    add     : -> throw "This collection does not support this method."
    remove  : -> throw "This collection does not support this method."
    reset   : -> throw "This collection does not support this method."
    set     : -> throw "This collection does not support this method."
    push    : -> throw "This collection does not support this method."
    pop     : -> throw "This collection does not support this method."
    unshift : -> throw "This collection does not support this method."
    shift   : -> throw "This collection does not support this method."
    fetch   : -> throw "This collection does not support this method."
    create  : -> throw "This collection does not support this method."


###
    A collection that is a subset of another collection.

    @arg models This should be left `null`. It is an argument here only to
        support the same constructor signature as other collections.
    @arg options Configuration for filtered collection.
        @option base_collection (required) Another collection to use as the
            source. Models that are exposed by this instance of
            `Collections.Filtered` will only come from `base_collection`.
        @option filter (optional) A function to use as the initial filter. This
            function should take a single argument, the model in question, and
            return `true` if that model should be exposed in this filtered
            collection. If this option is initially `null`, then all models from
            `base_collection` will be exposed.
###
class Collections.Filtered extends Collections.ReadOnly
    initialize: (models, options) ->
        super
        @_base_collection = options.base_collection
        @set_filter options.filter

        @listenTo @_base_collection, 'change', @_filter_model
        @listenTo @_base_collection, 'add',    @_on_add
        @listenTo @_base_collection, 'remove', @_on_remove

    _check_filter: (model) ->
        return not @_filter? or @_filter model

    _filter_model: (model, options) ->
        if @_check_filter model
            Backbone.Collection::set.call @, model, _.extend
                add    : true
                remove : false
                merge  : false
            , options
        else
            Backbone.Collection::remove.call @, model, options

    _on_add: (model, collection, options) ->
        if collection is @_base_collection
            @_filter_model model, options

    _on_remove: (model, collection, options) ->
        if collection is @_base_collection
            Backbone.Collection::remove.call @, model, options

    set_filter: (filter) ->
        @_filter = filter

        models = if @_filter? then @_base_collection.filter @_filter else @_base_collection.models
        Backbone.Collection::set.call @, models, {merge: false}

    # These functions forward the call to the underlying base_collection for
    # models that pass the filter. They all assume that "models" is either an
    # array of neatly parsed models or a singular properly instantiated model.

    add: (models, options) ->
        singular = not _.isArray models
        if singular
            if models? and @_check_filter models
                models = [models]
            else
                models = []
        else
            models = _.filter models, @_check_filter, @

        result = @_base_collection.add models, options

        if singular and result.length > 0
            return result[0]

        return result

    remove: (models, options) ->
        singular = not _.isArray models
        if singular
            if models? and @_check_filter models
                models = [models]
            else
                models = []
        else
            models = _.filter models, @_check_filter, @

        result = @_base_collection.remove models, options

        if singular and result.length > 0
            return result[0]

        return result
