Views = Tools.create_namespace 'Character.Views'


class Views.CharacterNumberTrait extends Backbone.View
    tagName: 'li'

    initialize: (options) ->
        @listenTo @model, 'change', @render

    events:
        'change input[name=\'rating\']' : 'save_rating'

    _change_field: (raw, field, construct) ->
        attr = {}
        attr[field] = if raw is '' then null else construct raw

        @model.save attr, { patch: true }

    save_rating: (e) ->
        @_change_field e.target.value, 'rating', (v) -> parseInt v, 10

    render: () ->
        @$el.html @options.template @model.toHumanJSON()
        @delegateEvents()
        @


class Views.NumberSection extends Backbone.View
    options:
        ItemView: Views.CharacterNumberTrait
        header: null

    render: () ->
        @$el.html @options.template { header: @options.header }
        @collection.each (item) ->
            @render_item item
        , @

    render_item: (model) ->
        view = new @options.ItemView
            model: model
            template: @options.item_template
        @$('.trait-list').append view.render().$el
        view
