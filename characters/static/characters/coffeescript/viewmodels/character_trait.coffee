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

        @available = {}
        if options.process_update_response?
            character_traits = ORM.characters.CharacterTrait.store()

            ## available traits

            @available.attribute = kb.collectionObservable ORM.traits.Attribute.store(), VM.traits.Trait
            @available.skill     = kb.collectionObservable ORM.traits.Skill.store(),     VM.traits.Trait

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

    new_trait: (model, options) ->
        # TODO (Emery): Better error handling.

        $.ajax "#{DCMS.Settings.URL_PREFIX}/characters/#{model.character.id}/character_trait/",
            method: 'POST'
            dataType: 'json'
            data: model.toJSON()
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
            data: model.toJSON()
            success: (data) =>
                @model().set (@model().parse data.character), 'synced': true
                @_process_update_response arguments...
            error: (jqXHR, status, exception) ->
                window.alert 'ERROR in delete_trait:\n' + status

    update_available_traits: (name, Model, data) ->
        Access = VM.traits.Trait.Access
        collection_observable = @available[name]
        CharacterModel = Tools.resolve "ORM.characters.Character#{Model.name}"

        create_trait = (attributes, access) ->
            trait = new Model attributes, 'parse': true
            collection_observable.collection().add trait
            view_model = collection_observable.viewModelByModel trait
            view_model.access access
            return [trait, view_model]

        for access, models of data
            access = Access[access]

            switch access
                when Access.FORCE
                    for attr in models
                        [trait, view_model] = create_trait attr, access
                        character_trait = CharacterModel.store().findWhere
                            'character_id': @id()
                            'trait_id': trait.id
                        if not character_trait?
                            character_trait = new CharacterModel
                                'character_id': @id()
                                'trait_id': trait.id

                when Access.ALLOW
                    for attr in models
                        create_trait attr, access

                when Access.DENY
                    for attr in models
                        create_trait attr, access
                        # TODO (Emery): (Make design decision.)
                        #   Should this automatically remove these traits from
                        #   the character? (like it does with "HIDE" below)

                when Access.HIDE
                    for trait in models
                        trait = Model.store().get attr.id

                        character_traits = CharacterModel.store().where
                            'character_id': @id()
                            'trait_id': trait.id

                        _.each character_traits, (character_trait) ->
                            character_trait.dismantle()

                        trait.dismantle()

        return
