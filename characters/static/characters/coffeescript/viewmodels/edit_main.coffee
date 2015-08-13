###
    @file  edit_main.coffee
    @brief Main view-models for character-edit page.
###


Tools.create_namespace 'VM.characters'
Tools.create_namespace 'VM.traits'


order_comparator = (a, b) ->
    a_order = a.trait().order()
    b_order = b.trait().order()
    return a_order - b_order

label_comparator = (a, b) ->
    a_label = a.trait().label()
    b_label = b.trait().label()
    return a_label.localeCompare b_label

trait_label_comparator = (a, b) ->
    return a.label().localeCompare b.label()


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
        up a nested view-model which parallels a model's has-one relationship.

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
    configure_has_many: (name, options) ->
        @[name] = kb.collectionObservable @model()[name], options


class VM.traits.Trait extends VM.BaseViewModel
    @Access: Tools.enum 'Access', [
        'FORCE'
        'ALLOW'
        'DENY'
        'HIDE'
    ]

    constructor: (model, options) ->
        super

        @access = ko.observable undefined

    copy: (other_vm) ->
        super
        @access other_vm?.access()
        return @


class VM.characters.CharacterTrait extends VM.BaseViewModel
    constructor: (model, options) ->
        super

        @configure_has_one 'trait', collection_observable: options.available_traits


class VM.characters.CharacterAttribute extends VM.characters.CharacterTrait
    constructor: (model, options) ->
        super

        @allowed_ratings = ko.observableArray [1, 2, 3, 4, 5]
        @allowed_ratings.sort()


class VM.characters.CharacterSkill extends VM.characters.CharacterTrait
    constructor: (model, options) ->
        super

        @allowed_ratings = ko.observableArray [0, 1, 2, 3, 4, 5]
        @allowed_ratings.sort()


class VM.characters.CharacterViewModel extends VM.BaseViewModel
    constructor: (model, options) ->
        # Kick this off right away so the server has as much time to process it
        # as possible as it might be an expensive operation.
        $.getJSON "#{ DCMS.Settings.URL_PREFIX }/characters/#{ model.id }/available_traits", null, => @process_update_response arguments...

        super

        ## available traits

        @available =
            creature_types : kb.collectionObservable ORM.traits.CreatureType.store(), VM.traits.Trait, sort_attribute: 'label'
            genealogies    : kb.collectionObservable ORM.traits.Genealogy.store(),    VM.traits.Trait, sort_attribute: 'label'
            affiliations   : kb.collectionObservable ORM.traits.Affiliation.store(),  VM.traits.Trait, sort_attribute: 'label'
            subgroups      : kb.collectionObservable ORM.traits.Subgroup.store(),     VM.traits.Trait, sort_attribute: 'label'

            attributes : kb.collectionObservable ORM.traits.Attribute.store(), VM.traits.Trait
            skills     : kb.collectionObservable ORM.traits.Skill.store(),     VM.traits.Trait,

        ## helper functions

        filter_attributes = (label) =>
            attribute_type = ORM.traits.AttributeType.store().findWhere 'label': label
            ViewModel = (model, options) =>
                new VM.characters.CharacterAttribute model, _.extend {}, options,
                    available_traits: @available.attributes
            return kb.collectionObservable @model().character_attributes, ViewModel,
                filters: (model) -> model.trait.attribute_type == attribute_type
                comparator: order_comparator

        filter_skills = (label) =>
            skill_type = ORM.traits.SkillType.store().findWhere 'label': label
            ViewModel = (model, options) =>
                new VM.characters.CharacterSkill model, _.extend {}, options,
                    available_traits: @available.skills
            return kb.collectionObservable @model().character_skills, ViewModel,
                filters: (model) -> model.trait.skill_type == skill_type
                comparator: label_comparator

        ## character summary traits

        model.on 'change', @update_summary_traits, @

        @configure_has_one 'user',      ViewModel : VM.auth.User
        @configure_has_one 'chronicle', ViewModel : VM.BaseViewModel

        @configure_has_one 'creature_type', collection_observable : @available.creature_types
        @configure_has_one 'genealogy',     collection_observable : @available.genealogies
        @configure_has_one 'affiliation',   collection_observable : @available.affiliations
        @configure_has_one 'subgroup',      collection_observable : @available.subgroups

        ## character traits

        @mental_attributes   = filter_attributes 'Mental'
        @physical_attributes = filter_attributes 'Physical'
        @social_attributes   = filter_attributes 'Social'

        @mental_skills   = filter_skills 'Mental'
        @physical_skills = filter_skills 'Physical'
        @social_skills   = filter_skills 'Social'

    disable_denied_traits: (option, view_model) ->
        if view_model?
            disable = view_model.access() is VM.traits.Trait.Access.DENY
        else
            disable = True
        ko.applyBindingsToNode option,
            'disable': disable

    update_summary_traits: (model, options) ->
        setTimeout (model, options) =>
            patch = model.changedAttributes()

            # HACK(Emery):

            #   As of now, not selecting an option in a <select> control gives a
            #   value of `undefined` as opposed to `null`. Remove these
            #   attributes from the update if the previous. Set these attributes
            #   to `null` if the previous value was not null. Find a way for the
            #   "options" binding to set unselected as `null` instead.
            for key in _.keys patch
                if patch[key] is undefined
                    if model.previousAttributes()[key] == null
                        delete patch[key]
                    else
                        patch[key] = null

            if _.keys(patch).length
                $.ajax "#{ DCMS.Settings.URL_PREFIX }/characters/#{ model.id }/update_summary",
                    method: 'PATCH'
                    dataType: 'json'
                    data: patch
                    success: => @process_update_response arguments...
                    error: (jqXHR, status, exception) ->
                        window.alert 'ERROR in update_summary_traits:\n' + status
        , 1, model, options

    process_update_response: (data) ->
        for Model, model_groups of data
            Model = ORM.traits[Model]

            switch Model
                when ORM.traits.CreatureType then @update_available_summary_traits 'creature_type', Model, @available.creature_types, model_groups
                when ORM.traits.Genealogy    then @update_available_summary_traits 'genealogy',     Model, @available.genealogies,    model_groups
                when ORM.traits.Affiliation  then @update_available_summary_traits 'affiliation',   Model, @available.affiliations,   model_groups
                when ORM.traits.Subgroup     then @update_available_summary_traits 'subgroup',      Model, @available.subgroups,      model_groups
                # TODO(Emery): Update other available traits.

    update_available_summary_traits: (name, Model, collection_observable, data) ->
        Access = VM.traits.Trait.Access

        create = (attributes, access) ->
            trait = new Model attributes, 'parse': true
            collection_observable.collection().add trait
            view_model = collection_observable.viewModelByModel trait
            view_model.access access
            return [trait, view_model]

        for access, models of data
            access = Access[access]

            switch access
                when Access.FORCE
                    # TODO(Emery): enforce that this model list only has one item
                    [trait, view_model] = create models[0], access
                    @[name] view_model

                when Access.ALLOW
                    for attr in models
                        create attr, access

                when Access.DENY
                    for attr in models
                        create attr, access
                        # TODO(Emery): (Make design decision.)
                        #   Should this automatically remove these traits from
                        #   the character? (like it does with "HIDE" below)

                when Access.HIDE
                    for attr in models
                        trait = Model.store().findWhere 'id': attr.id

                        if trait is @model()[name]
                            if Model is ORM.traits.CreatureType
                                creature_type_mortal = Model.store().findWhere 'name': 'CREATURE_TYPE_MORTAL'
                                @model().creature_type = creature_type_mortal
                            else
                                @model()[name] = null

                        trait?.dismantle()

        return
