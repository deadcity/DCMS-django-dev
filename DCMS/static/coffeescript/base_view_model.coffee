###
    @file  base_view_model.coffee
    @brief Base view-model class for DCMS View-Models.
###


Tools.create_namespace 'VM'


class VM.BaseViewModel extends kb.ViewModel
    ###
        Copy the observable members of `other_vm`.

        @arg other_vm The source view-model to copy from. If `other_vm` is
            `null`, then this method will set all observables to `null`.

        This is not a copy-constructor. It must be called from a pre-existing
        instance.

        The class of `other_vm` must match the class of the calling instance. If
        a class inheriting from this class defines more members that are
        observables, it is responsible for overriding this method, calling super
        and then copying those extra observables.
    ###
    copy: (other_vm) ->
        if not other_vm?
            @model null
            return @

        if @constructor isnt other_vm.constructor
            throw "Cannot copy observables from a different class of view-model."

        @model other_vm.model()
        return @

    ###
        Create a computed-observable of a view-model that manages a model
        referenced by this view-model's model. In other words, this method sets
        up a nested view-model which parallels a model's "has-one" relation.

        @arg name A string identifying the attribute through which we can access
            the target model from this view-model's model.
        @arg options Configuration for the view-model observable.
            @option ViewModel (required if `collection_observable` is not
                specified) Identifies the class used to generate the view-model
                instance. If `collection_observable` is specified and
                `ViewModel` is not, `configure_has_one` will use the same view-
                model that `collection_observable` uses.
            @option collection_observable A knockback CollectionObservable from
                which the target view-model will be coppied. It is assumed that
                the only possible values for the resultant view-model's model
                are those represented in `collection_observable`. The resultant
                view-model will always be a copy of one of the view-models found
                in `collection_observable` and never one of the actual view-
                models from that collection.
    ###
    configure_has_one: (name, options) ->
        referenced_model = @model()[name]
        relation_options = @model().constructor.relations().one[name]
        if _.isString relation_options.Model
            relation_options.Model = Tools.resolve relation_options.Model
        attribute = relation_options.attribute

        # Identify the class for the for the target view-model.
        if options.ViewModel?
            ViewModel = options.ViewModel
        else
            collection = options.collection_observable
            ViewModel = collection.shareOptions().factory.paths.models
        sub_vm = new ViewModel referenced_model

        # Create reader functions for the observable.
        if options.collection_observable?
            read = =>
                @[attribute]()
                referenced_model = @model()[name]
                if referenced_model?
                    other_sub_vm = collection.viewModelByModel referenced_model
                    sub_vm.copy other_sub_vm
                else
                    sub_vm.copy null
                return sub_vm
        else
            read = =>
                @[attribute]()
                sub_vm.model @model()[name]
                return sub_vm

        # Create the observable.
        @[name] = ko.computed
            read: read
            write: (other_sub_vm) =>
                # In knockout.js, if a select data-bind includes the parameter
                # optionsValue, then the value returned to set the observable is
                # that value rather than the bound view-model. We need to obtain
                # the viewmodel before we continue.
                if _.isNumber other_sub_vm
                    Model = relation_options.Model
                    model = Model.store().get other_sub_vm
                    other_sub_vm = collection.viewModelByModel model

                sub_vm.copy other_sub_vm
                # NOTE: Do not change this to `other_sub_vm?.model()`.
                #   `@model()[name]` should never be set to `null`.
                @model()[name] = if other_sub_vm? then other_sub_vm.model() else null

    ###
        Create a knockback CollectionObservable over the collection representing
        a "has-many" relation.
    ###
    configure_has_many: (name, ViewModel, options) ->
        options = _.defaults {}, options#,
            # viewmodel_options: {}

        if options?.viewmodel_options?
            viewmodel_options = options.viewmodel_options
            VM_Constructor = (model, options) ->
                opts = _.defaults {}, viewmodel_options, options
                new ViewModel model, opts
        else
            VM_Constructor = ViewModel
        @[name] = kb.collectionObservable @model()[name], VM_Constructor, options
