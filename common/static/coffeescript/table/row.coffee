Models_NS = Tools.create_namespace 'Table.Models'
Views_NS  = Tools.create_namespace 'Table.Views'


class Models_NS.RowPresentation extends Backbone.Model
    defaults:
        selected: false

    initialize: (attributes, options) ->
        @record = options.record
        @listenTo @record, 'destroy', @destroy
        @listenTo @record, 'remove',  @destroy
        @on 'destroy', @on_destroy, @

    toJSON: () ->
        attr = _.clone @attributes
        attr.record = (@record.toHumanJSON ? @record.toJSON).apply @record
        attr

    on_destroy: () ->
        @stopListening()


###
  A basic view for a table row.  Renders simply from a template.  Extend to
  specify the template.

  @prop model - underlying row presentation model
###

class Views_NS.Row extends Backbone.View
    tagName: 'tr'

    template: null

    initialize: (options) ->
        if options?.template?
            @template = options.template

        @listenTo @model, 'destroy', @remove
        @listenTo @model, 'remove',  @remove
        @listenTo @model.record, 'change', @render

        @listenTo @model, 'change:selected', @on_selected
        @listenTo @model, 'command:move_to', @move_to
        @listenTo @model, 'hide',            @remove

    events: () ->
        'click': 'on_click'

    render: () ->
        @$el.html @template @model.toJSON()
        @delegateEvents()
        @

    on_click: (event) ->
        @model.set 'selected', not @model.get('selected'), {event: event}

    on_selected: (model, value, options) ->
        if model.get 'selected'
            @$el.addClass 'selected'
        else
            @$el.removeClass 'selected'

    move_to: (parent, idx, parent_view) ->
        @$el.detach()
        if idx == -1
            @$el.appendTo parent
            return

        other_rows = $ @tagName, parent
        if other_rows.length <= idx
            @$el.appendTo parent
        else
            @$el.insertBefore other_rows[idx]
