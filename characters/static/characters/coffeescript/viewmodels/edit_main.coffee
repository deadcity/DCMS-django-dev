###
    @file  edit_main.coffee
    @brief Main view-models for character-edit page.
###


Tools.create_namespace 'VM.characters'


order_comparator = (a, b) ->
    a_order = a.trait().order()
    b_order = b.trait().order()
    return a_order - b_order

order_label = (a, b) ->
    a_label = a.trait().label()
    b_label = b.trait().label()
    return a_label.localeCompare b_label


class VM.characters.AttributeViewModel extends kb.ViewModel
    constructor: (model, options) ->
        super

        @allowed_ratings = ko.observableArray [1, 2, 3, 4, 5]
        @allowed_ratings.sort()


class VM.characters.SkillViewModel extends kb.ViewModel
    constructor: (model, options) ->
        super

        @allowed_ratings = ko.observableArray [0, 1, 2, 3, 4, 5]
        @allowed_ratings.sort()


class VM.characters.CharacterViewModel extends kb.ViewModel
    constructor: (model, options) ->
        super model, _.extend {}, options,
            factories:
                'user' : VM.auth.User

        filter_attributes = (label) =>
            attribute_type = ORM.traits.AttributeType.all().findWhere 'label': label
            return kb.collectionObservable @model().character_attributes(), VM.characters.CharacterAttributeViewModel,
                filters: (model) -> model.trait().attribute_type() == attribute_type
                comparator: order_comparator

        filter_skills = (label) =>
            skill_type = ORM.traits.SkillType.all().findWhere 'label': label
            return kb.collectionObservable @model().character_skills(), VM.characters.CharacterSkillViewModel,
                filters: (model) -> model.trait().skill_type() == skill_type
                comparator: order_label

        @mental_attributes   = filter_attributes 'Mental'
        @physical_attributes = filter_attributes 'Physical'
        @social_attributes   = filter_attributes 'Social'

        @mental_skills   = filter_skills 'Mental'
        @physical_skills = filter_skills 'Physical'
        @social_skills   = filter_skills 'Social'


        # # # # # # # # # # #
        # AVAILABLE TRAITS  #
        # # # # # # # # # # #

        @available_creature_types = kb.collectionObservable [model.creature_type()], comparator: 'order'
        @available_genealogies    = kb.collectionObservable [model.genealogy()],     comparator: 'order'
        @available_affiliations   = kb.collectionObservable [model.affiliation()],   comparator: 'order'
        @available_subgroups      = kb.collectionObservable [model.subgroup()],      comparator: 'order'
