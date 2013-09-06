Collections = Tools.create_namespace 'Tools.Collections'


class Collections.FilteredCollection extends Backbone.Collection
    initialize: (models, options) ->
        super models, options
        @_base_collection = options.base_collection
        @filter options.filter

        @listenTo @_base_collection, 'change', @_filter_model
        @listenTo @_base_collection, 'add',    @_on_add
        @listenTo @_base_collection, 'remove', @_on_remove

    _filter_model: (model, options) ->
        if not @_filter? or @_filter model
            @add model, options
        else
            @remove model, options

    _on_add: (model, collection, options) ->
        if collection is @_base_collection
            @_filter_model model, options

    _on_remove: (model, collection, options) ->
        if collection is @_base_collection
            @remove model, options

    filter: (filter) ->
        @_filter = filter

        models = if @_filter? then @_base_collection.filter @_filter else @_base_collection.models
        @set models, {merge: false}
