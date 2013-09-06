Views_NS = Tools.create_namespace 'Character.Views'


option_template = _.template '<option value="<%= id %>"<% if (selected) { %> selected<% } %>><%= name %></option>'


class Views_NS.CharacterSummary extends Backbone.View
    tagName: 'section'

    initialize: (options) ->
        @template = options.template

    events: () ->
        return {
            'change input[name="status"]'       : 'on_change_status'
            'change input[name="name"]'         : 'on_change_name'
            'change select[name="genealogy"]'   : 'on_change_genealogy'
            'change select[name="affiliation"]' : 'on_change_affiliation'
            'change select[name="subgroup"]'    : 'on_change_subgroup'
            'change select[name="virtue"]'      : 'on_change_virtue'
            'change select[name="vice"]'        : 'on_change_vice'
        }

    _change_field: (e, field, construct) ->
        attr = {}
        attr[field] = e.target.value
        if attr[field] == '' then attr[field] = null

        @model.save attr, patch: true

    on_change_status: (e) ->
        @_change_field e, 'status', (v) -> v

    on_change_name: (e) ->
        @_change_field e, 'name', (v) -> v

    on_change_genealogy: (e) ->
        @_change_field e, 'genealogy', (v) -> Traits.Objects.Genealogy.get v

    on_change_affiliation: (e) ->
        @_change_field e, 'affiliation', (v) -> Traits.Objects.Affiliation.get v

    on_change_subgroup: (e) ->
        @_change_field e, 'subgroup', (v) -> Traits.Objects.Subgroup.get v

    on_change_virtue: (e) ->
        @_change_field e, 'virtue', (v) -> Traits.Enums.Virtue.get v

    on_change_vice: (e) ->
        @_change_field e, 'vice', (v) -> Traits.Enums.Vice.get v

    render: () ->
        @$el.html @template @model.toHumanJSON()

        # Available genealogies.
        Traits.Objects.Genealogy.each (item) ->
            context = item.toHumanJSON()
            context.selected = item == @model.get 'genealogy'
            @$('[name="genealogy"]').append option_template context
        , @

        # Available affiliations.
        Traits.Objects.Affiliation.each (item) ->
            context = item.toHumanJSON()
            context.selected = item == @model.get 'affiliation'
            @$('[name="affiliation"]').append option_template context
        , @

        # Available subgroups.
        Traits.Objects.Subgroup.each (item) ->
            context = item.toHumanJSON()
            context.selected = item == @model.get 'subgroup'
            @$('[name="subgroup"]').append option_template context
        , @

        # Available virtues.
        _.each Traits.Enums.Virtue._elements, (item) ->
            context = item.toJSON()
            context.selected = item == @model.get 'virtue'
            @$('[name="virtue"]').append option_template context
        , @

        # Available vices.
        _.each Traits.Enums.Vice._elements, (item) ->
            context = item.toJSON()
            context.selected = item == @model.get 'vice'
            @$('[name="vice"]').append option_template context
        , @
