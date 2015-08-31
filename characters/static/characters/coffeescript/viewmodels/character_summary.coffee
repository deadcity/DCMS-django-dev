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

        @available = VM.trait_access.AvailableTraits

        ## register sync events
        if options.process_update_response?
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
