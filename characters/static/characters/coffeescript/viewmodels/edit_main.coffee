###
    @file  edit_main.coffee
    @brief Main view-models for character-edit page.
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

trait_label_comparator = (a, b) ->
    return a.label().localeCompare b.label()


class VM.characters.CharacterViewModel extends VM.BaseViewModel
    constructor: (model, options) ->
        # Kick this off right away so the server has as much time to process it
        # as possible as it might be an expensive operation.
        $.getJSON "#{ DCMS.Settings.URL_PREFIX }/characters/#{ model.id }/available_traits", => @process_update_response arguments...

        super

        sub_vm_options = process_update_response: => @process_update_response arguments...
        @character_summary = new VM.characters.CharacterSummary @model(), sub_vm_options
        @character_details = new VM.characters.CharacterDetails @model(), sub_vm_options

    disable_denied_traits: (option, view_model) ->
        if view_model?
            disable = view_model.access() is VM.traits.Trait.Access.DENY
        else
            # Disable the placeholder option.
            disable = True
        ko.applyBindingsToNode option,
            'disable': disable

    process_update_response: (data) ->
        for Model, model_groups of data.availabilities
            Model = ORM.traits[Model]

            switch Model
                when ORM.traits.CreatureType then @character_summary.update_available_summary_traits 'creature_type', model_groups
                when ORM.traits.Genealogy    then @character_summary.update_available_summary_traits 'genealogy',     model_groups
                when ORM.traits.Affiliation  then @character_summary.update_available_summary_traits 'affiliation',   model_groups
                when ORM.traits.Subgroup     then @character_summary.update_available_summary_traits 'subgroup',      model_groups

                when ORM.traits.Attibute then @character_details.update_available_traits 'attribute', ORM.traits.Attibute, model_groups
                when ORM.traits.Skill    then @character_details.update_available_traits 'skill',     ORM.traits.Skill,    model_groups

        return
