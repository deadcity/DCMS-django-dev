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
        super

        attribute_type_mental   = ORM.traits.AttributeType.all().findWhere label: 'Mental'
        attribute_type_social   = ORM.traits.AttributeType.all().findWhere label: 'Social'
        attribute_type_physical = ORM.traits.AttributeType.all().findWhere label: 'Physical'

        skill_type_mental   = ORM.traits.SkillType.all().findWhere label: 'Mental'
        skill_type_social   = ORM.traits.SkillType.all().findWhere label: 'Social'
        skill_type_physical = ORM.traits.SkillType.all().findWhere label: 'Physical'

        @player_name = ko.computed =>
            user = @user()
            if user.first_name()? or user.last_name()?
                player_name = ((user.first_name() ? '') + ' ' + (user.last_name() ? '')).trim()
                return player_name if player_name != ''
            return user.username().trim()

        @mental_attributes = kb.collectionObservable @model().character_attributes(), VM.characters.AttributeViewModel,
            filters: (model) -> model.trait().attribute_type() == attribute_type_mental
            comparator: order_comparator
        @physical_attributes = kb.collectionObservable @model().character_attributes(), VM.characters.AttributeViewModel,
            filters: (model) -> model.trait().attribute_type() == attribute_type_physical
            comparator: order_comparator
        @social_attributes = kb.collectionObservable @model().character_attributes(), VM.characters.AttributeViewModel,
            filters: (model) -> model.trait().attribute_type() == attribute_type_social
            comparator: order_comparator

        @mental_skills = kb.collectionObservable @model().character_skills(), VM.characters.SkillViewModel,
            filters: (model) -> model.trait().skill_type() == skill_type_mental
            comparator: order_label
        @physical_skills = kb.collectionObservable @model().character_skills(), VM.characters.SkillViewModel,
            filters: (model) -> model.trait().skill_type() == skill_type_physical
            comparator: order_label
        @social_skills = kb.collectionObservable @model().character_skills(), VM.characters.SkillViewModel,
            filters: (model) -> model.trait().skill_type() == skill_type_social
            comparator: order_label
