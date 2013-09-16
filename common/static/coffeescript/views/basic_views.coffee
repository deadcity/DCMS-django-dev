Views = Tools.create_namespace 'Common.Views'


class Views.Item extends Backbone.View
    options:
        template: null

    initialize: (options) ->
        @listenTo @model, 'change',  @render
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'destroy', @remove

    events: () ->
        'click .remove' : 'delete_item'

    render: (model, options) ->
        if options?.source is @
            return @

        @$el.html @options.template @model.toHumanJSON()
        @delegateEvents()
        @

    delete_item: () ->
        @model.destroy()


class Views.Control extends Views.Item
    _change_field: (field, raw, options) ->
        options = _.extend
            patch: true
            source: @
            construct: @_constructors.nullable
        , options ? {}

        if _.has options, 'construct'
            construct = construct
            delete options.construct
        else
            construct = null

        attr = {}
        attr[field] = if construct? then construct raw else raw
        @model.save attr, options

    _constructors:
        int: (v) -> if v is '' then null else parseInt v, 10
        nullable: (v) -> if v is '' then null else v


class Views.List extends Backbone.View
    options:
        ItemView      : Views.Item
        item_options  : null
        template      : null
        template_data : null
        list_selector : 'ul'

    initialize: (options) ->
        @listenTo @collection, 'add', @render_item

    render: () ->
        @$el.html @options.template @options.template_data
        @collection.each (item) ->
            @render_item item
        , @

    render_item: (model) ->
        options = _.defaults {}, @options.item_options,
            model: model
            tagName: 'li'

        view = new @options.ItemView options
        @$(@options.list_selector).append view.render().$el
        view


class Views.ListSelection extends Views.List
    options: _.extend({}, Views.List.prototype.options, {
        groups: null
        group_template: _.template '<optgroup label=\'<%= name %>\'></optgroup>'
        option_template: _.template '<option value=\'<%= id %>\'><%= name %></option>'
        select_selector: 'select'
    })

    events: () ->
        {
            'click button[name=\'add\']': 'add_item'
        }

    render: () ->
        super

        select = @$ @options.select_selector

        _.each _.pairs(@options.groups), (pair) ->
            if pair[0] is 'null'
                _.each pair[1], (item) =>
                    select.append @options.option_template item.toHumanJSON()
            else
                group_element = $ @options.group_template { name: pair[0] }
                _.each pair[1], (item) =>
                    group_element.append @options.option_template item.toHumanJSON()
                select.append group_element
        , @
        @
