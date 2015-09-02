###
    @file  character_trait.coffee
    @brief View-models and related objects for character-traits.
###


Tools.create_namespace 'VM.characters'


order_comparator = (a, b) ->
    a_order = a.trait().order()
    b_order = b.trait().order()
    return a_order - b_order

label_comparator = (a, b) ->
    a_label = a.trait().label()
    b_label = b.trait().label()
    return a_label.localeCompare b_label


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


class VM.characters.CharacterDetails extends VM.BaseViewModel
    constructor: (model, options) ->
        options = _.defaults {}, options,
            process_update_response: null

        super model, options
        @_process_update_response = options.process_update_response

        @available = VM.trait_access.AvailableTraits
        if options.process_update_response?
            character_traits = ORM.characters.CharacterTrait.store()

            ## register sync events

            character_traits.on 'add',     (trait, store, options) => @new_trait    trait, options
            character_traits.on 'change',  (trait, store, options) => @update_trait trait, options
            character_traits.on 'destroy', (trait, store, options) => @delete_trait trait, options

        ## helper functions

        filter_traits_by_type = (trait_type, trait_type_name, ViewModel, available_traits, source, comparator = order_comparator) =>
            VM_constructor = (model, options) ->
                new ViewModel model, _.extend {}, options,
                    'available_traits': available_traits
            return kb.collectionObservable source, VM_constructor,
                'filters': (model) -> model.trait[trait_type_name] == trait_type
                'comparator': comparator

        filter_attributes = (label) =>
            filter_traits_by_type(
                ORM.traits.AttributeType.store().findWhere('label': label),
                'attribute_type'
                VM.characters.CharacterAttribute,
                @available.attribute,
                @model().character_attributes
            )

        filter_skills = (label) =>
            filter_traits_by_type(
                ORM.traits.SkillType.store().findWhere('label': label),
                'skill_type',
                VM.characters.CharacterSkill,
                @available.skill,
                @model().character_skills,
                label_comparator
            )

        ## character traits

        @mental_attributes   = filter_attributes 'Mental'
        @physical_attributes = filter_attributes 'Physical'
        @social_attributes   = filter_attributes 'Social'

        @mental_skills   = filter_skills 'Mental'
        @physical_skills = filter_skills 'Physical'
        @social_skills   = filter_skills 'Social'

        @skill_specialty_skill = ko.observable()
        @skill_specialty_text = ko.observable()
        @configure_has_many 'character_skill_specialties', VM.characters.CharacterTrait,
            'viewmodel_options':
                'available_traits': @available.skill

        @power_name = ko.computed =>
            power_name = @model().creature_type?.get 'power_name'
            return null if power_name is null
            return "#{power_name[0].toUpperCase()}#{power_name.slice 1}s"
        @selected_power = ko.observable()
        @configure_has_many 'character_powers', VM.characters.CharacterTrait,
            'viewmodel_options':
                'available_traits': @available.power

    add_skill_specialty: () ->
        specialty = new ORM.characters.CharacterSkillSpecialty
            'character_id' : @model().id
            'trait_id'     : @skill_specialty_skill().trait().id()
            'specialty'    : @skill_specialty_text()

    add_power: () ->
        power = new ORM.characters.CharacterPower
            'character_id' : @model().id
            'trait_id'     : @selected_power().id()

    remove_trait: (view_model) ->
        view_model.model().dismantle()

    new_trait: (model, options) ->
        # TODO (Emery): Better error handling.

        $.ajax "#{DCMS.Settings.URL_PREFIX}/characters/#{model.character.id}/character_trait/",
            method: 'POST'
            dataType: 'json'
            data: JSON.stringify model.toJSON()
            success: (data) =>
                @model().set (@model().parse data.character), 'synced': true
                model.set (model.parse data.model), 'synced': true
                @_process_update_response arguments...
            error: (jqXHR, status, exception) ->
                window.alert 'ERROR in new_trait:\n' + status

    update_trait: (model, options) ->
        # Use `setTimeout` with a delay of 1 ms instead of executing this code
        # immediately to allow any queued events to finish processing first.
        setTimeout (model, options) =>
            patch = model.changedAttributes()

            # # Ignore updates to `id` field.
            # if patch.id?
            #     delete patch.id

            # TODO (Emery): Better error handling.

            if _.keys(patch).length and not options?.synced
                $.ajax "#{DCMS.Settings.URL_PREFIX}/characters/#{model.character.id}/character_trait/#{model.id}",
                    method: 'PATCH'
                    dataType: 'json'
                    data: JSON.stringify patch
                    success: (data) =>
                        @model().set (@model().parse data.character), 'synced': true
                        model.set (model.parse data.model), 'synced': true
                        @_process_update_response arguments...
                    error: (jqXHR, status, exception) ->
                        window.alert 'ERROR in update_trait:\n' + status
        , 1, model, options

    delete_trait: (model, options) ->
        # TODO (Emery): Better error handling.

        $.ajax "#{DCMS.Settings.URL_PREFIX}/characters/#{model.character.id}/character_trait/#{model.id}",
            method: 'DELETE'
            datatype: 'json'
            data: JSON.stringify model.toJSON()
            success: (data) =>
                @model().set (@model().parse data.character), 'synced': true
                @_process_update_response arguments...
            error: (jqXHR, status, exception) ->
                window.alert 'ERROR in delete_trait:\n' + status
