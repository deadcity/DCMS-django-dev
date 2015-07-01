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
    copy: (other_vm) ->
        if not other_vm?
            @model null
            return @

        if @constructor isnt other_vm.constructor
            throw "Cannot copy observables from a different class of view-model."

        @model other_vm.model()
        return @

    configure_has_one: (name, options) ->
        referenced_model = @model()[name]
        attribute = @model().constructor.relations().one[name].attribute

        if options.ViewModel?
            ViewModel = options.ViewModel
            sub_vm = new ViewModel referenced_model
            read = =>
                @[attribute]()
                sub_vm.model @model()[name]
                return sub_vm

        else
            collection = options.collection_observable
            ViewModel = collection.shareOptions().factory.paths.models
            sub_vm = new ViewModel referenced_model
            read = =>
                @[attribute]()
                referenced_model = @model()[name]
                if referenced_model?
                    other_sub_vm = collection.viewModelByModel referenced_model
                    sub_vm.copy other_sub_vm
                else
                    sub_vm.copy null
                return sub_vm

        @[name] = ko.computed
            read: read
            write: (other_sub_vm) =>
                sub_vm.copy other_sub_vm
                @model()[name] = other_sub_vm.model()

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

    update_summary_traits: (model, options) ->
        setTimeout (model, options) =>
            patch = model.changedAttributes()
            if patch
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
            view_model = collection_observable.viewModelByModel trait
            if not view_model?
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
                        # TODO(Emery): Should this automatically remove these
                        #              traits from the character? (like it does
                        #              with "HIDE" below)

                when Access.HIDE
                    for attr in models
                        trait = Model.store().findWhere 'id': attr.id

                        if trait is @model()[name]
                            if Model is ORM.traits.CreatureType
                                creature_type_mortal = Model.store().findWhere 'name': 'CREATURE_TYPE_MORTAL'
                                @model().creature_type = creature_type_mortal
                            else
                                @model()[name] null

                        trait.dismantle()
