###
    @file  character_summary.coffee
    @brief Main view-model for character summary. (name, creature-type, ...)
###


Tools.create_namespace 'VM.characters'


class VM.characters.CharacterSummary extends VM.BaseViewModel
    constructor: (model, options) ->
        options = _.defaults {}, options,
            process_update_response: null

        super model, options
        @_process_update_response = options.process_update_response

        @available = {}
        if options.process_update_response?

            ## available traits

            @available.creature_type = kb.collectionObservable ORM.traits.CreatureType.store(), VM.traits.Trait, sort_attribute: 'label'
            @available.genealogy     = kb.collectionObservable ORM.traits.Genealogy.store(),    VM.traits.Trait, sort_attribute: 'label'
            @available.affiliation   = kb.collectionObservable ORM.traits.Affiliation.store(),  VM.traits.Trait, sort_attribute: 'label'
            @available.subgroup      = kb.collectionObservable ORM.traits.Subgroup.store(),     VM.traits.Trait, sort_attribute: 'label'

            ## register sync events

            model.on 'change', @update_summary_traits, @

        ## character summary traits

        @configure_has_one 'user',      ViewModel : VM.auth.User
        @configure_has_one 'chronicle', ViewModel : VM.BaseViewModel

        @configure_has_one 'creature_type', collection_observable : @available.creature_type
        @configure_has_one 'genealogy',     collection_observable : @available.genealogy
        @configure_has_one 'affiliation',   collection_observable : @available.affiliation
        @configure_has_one 'subgroup',      collection_observable : @available.subgroup

    update_summary_traits: (model, options) ->
        # Use `setTimeout` with a delay of 1 ms instead of executing this code
        # immediately to allow any queued events to finish processing first.
        setTimeout (model, options) =>
            patch = model.changedAttributes()

            # HACK (Emery): As of now, not selecting an option in a <select>
            #   control managed by knockout gives a value of `undefined` as
            #   opposed to `null`. Remove these attributes from the update if
            #   the previous value was `null`. Set these attributes to `null` if
            #   the previous value was not `null`.

            # TODO (Emery): Find a way for the "options" binding to set
            #   unselected values as `null` instead.

            for key in _.keys patch
                if patch[key] is undefined
                    if model.previousAttributes()[key] == null
                        delete patch[key]
                    else
                        patch[key] = null

            # TODO (Emery): Better error handling.

            if _.keys(patch).length and not options.synced
                $.ajax "#{DCMS.Settings.URL_PREFIX}/characters/#{model.id}/update_summary",
                    method: 'PATCH'
                    dataType: 'json'
                    data: JSON.stringify patch
                    success: (data) =>
                        model.set (model.parse data.character), 'synced': true
                        @_process_update_response arguments...
                    error: (jqXHR, status, exception) ->
                        window.alert 'ERROR in update_summary_traits:\n' + status
        , 1, model, options

    update_available_summary_traits: (name, data) ->
        relation_options = @model().constructor.relations().one[name]
        if _.isString relation_options.Model
            relation_options.Model = Tools.resolve relation_options.Model

        Access = VM.traits.Trait.Access
        Model = relation_options.Model
        collection_observable = @available[name]

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
                    # TODO (Emery): enforce that this model list only has one item.
                    [trait, view_model] = create models[0], access
                    @[name] view_model

                when Access.ALLOW
                    for attr in models
                        create attr, access

                when Access.DENY
                    for attr in models
                        create attr, access
                        # TODO (Emery): (Make design decision.)
                        #   Should this automatically remove these traits from
                        #   the character? (like it does with "HIDE" below)

                when Access.HIDE
                    for attr in models
                        trait = Model.store().get attr.id

                        if trait is @model()[name]
                            if Model is ORM.traits.CreatureType
                                creature_type_mortal = Model.store().findWhere 'name': 'CREATURE_TYPE_MORTAL'
                                @model().creature_type = creature_type_mortal
                            else
                                @model()[name] = null

                        trait?.dismantle()

        return
