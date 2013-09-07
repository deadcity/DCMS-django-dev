Views_NS = Tools.create_namespace 'Character.Views'


class Views_NS.AttributeGroup extends Backbone.View
    tagname: 'div'

    initialize: (options) ->
        options = options ? {}
        @header = options.header
        @template = options.template
        @ItemView = options.ItemView

    render: () ->
        @$el.html @template {header: @header}
        @collection.each (item) ->
            view = new @ItemView
                model: item
                values: @options.values
            @$('.trait-list').append view.render().$el
        , @
        @


attribute_template = _.template "<span class='stat-label'><%= trait.name %></span><div class='rating-container'></div>"


class Views_NS.EditAttribute extends Backbone.View
    tagName: 'li'

    render: () ->
        @$el.html attribute_template @model.toHumanJSON()
        @rating = new Rating.Rating
            el:    @$ 'div'
            field: 'rating'
            model: @model
            values: @options.values
            patch: true
        @rating.render()
        @
