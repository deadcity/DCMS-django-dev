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


class VM.traits.Trait extends kb.ViewModel
    @Access: Tools.enum 'Access', [
        'FORCE'
        'ALLOW'
        'DENY'
        'HIDE'
    ]

    constructor: (model, options) ->
        super

        @access = ko.observable undefined


class VM.characters.CharacterAttribute extends kb.ViewModel
    constructor: (model, options) ->
        super

        @allowed_ratings = ko.observableArray [1, 2, 3, 4, 5]
        @allowed_ratings.sort()


class VM.characters.CharacterSkill extends kb.ViewModel
    constructor: (model, options) ->
        super

        @allowed_ratings = ko.observableArray [0, 1, 2, 3, 4, 5]
        @allowed_ratings.sort()


class VM.characters.CharacterViewModel extends kb.ViewModel
    available: undefined

    constructor: (model, options) ->
        super model, _.extend {}, options,
            factories:
                'user' : VM.auth.User

        model.on 'change', @update_summary_traits, @

        filter_attributes = (label) =>
            attribute_type = ORM.traits.AttributeType.all().findWhere 'label': label
            return kb.collectionObservable @model().character_attributes(), VM.characters.CharacterAttribute,
                filters: (model) -> model.trait().attribute_type() == attribute_type
                comparator: order_comparator

        filter_skills = (label) =>
            skill_type = ORM.traits.SkillType.all().findWhere 'label': label
            return kb.collectionObservable @model().character_skills(), VM.characters.CharacterSkill,
                filters: (model) -> model.trait().skill_type() == skill_type
                comparator: label_comparator

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
                    # method: 'PATCH'
                    method: 'PUT'
                    dataType: 'json'
                    data: patch
                    success: => @available.process_update arguments...
                    error: (jqXHR, status, exception) ->
                        window.alert 'ERROR in update_summary_traits:\n' + status
        , 1, model, options


class VM.characters.AvailableTraits
    # Instance of VM.characters.CharacterViewModel
    character: undefined

    constructor: (model) ->
        @creature_types = if model.creature_type()? then [model.creature_type()] else []
        @genealogies    = if model.genealogy()?     then [model.genealogy()]     else []
        @affiliations   = if model.affiliation()?   then [model.affiliation()]   else []
        @subgroups      = if model.subgroup()?      then [model.subgroup()]      else []

        @creature_types = kb.collectionObservable @creature_types, VM.traits.Trait, comparator: trait_label_comparator
        @genealogies    = kb.collectionObservable @genealogies,    VM.traits.Trait, comparator: trait_label_comparator
        @affiliations   = kb.collectionObservable @affiliations,   VM.traits.Trait, comparator: trait_label_comparator
        @subgroups      = kb.collectionObservable @subgroups,      VM.traits.Trait, comparator: trait_label_comparator

        $.getJSON "#{ DCMS.Settings.URL_PREFIX }/characters/#{ model.id }/available_traits", null, => @process_update arguments...

    # get_all_available_traits: () ->
    #     $.getJSON "#{ DCMS.Settings.URL_PREFIX }/characters/#{ model.id }/available_traits", null, => @process_update arguments...

    process_update: (data) ->
        for Model, model_groups of data
            Model = ORM.traits[Model]

            switch Model
                when ORM.traits.CreatureType then @update_summary_traits Model, @creature_types, model_groups, @character.creature_type
                when ORM.traits.Genealogy    then @update_summary_traits Model, @genealogies,    model_groups, @character.genealogy
                when ORM.traits.Affiliation  then @update_summary_traits Model, @affiliations,   model_groups, @character.affiliation
                when ORM.traits.Subgroup     then @update_summary_traits Model, @subgroups,      model_groups, @character.subgroup

    update_summary_traits: (Model, collection_observable, data, observable) ->
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
                    observable trait

                when Access.ALLOW
                    for attr in models
                        create attr, access

                when Access.DENY
                    for attr in models
                        create attr, access

                when Access.HIDE
                    for attr in models
                        trait = Model.all().findWhere 'id': attr.id

                        if trait is observable()
                            if Model is ORM.traits.CreatureType
                                observable ORM.traits.CreatureType.all().findWhere 'name': 'CREATURE_TYPE_MORTAL'
                            else
                                observable null

                        trait.dismantle()
