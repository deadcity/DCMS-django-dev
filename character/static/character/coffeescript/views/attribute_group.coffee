Views = Tools.create_namespace 'Character.Views'


attribute_template = _.template "<span class='stat-label'><%= trait.name %></span><div class='rating-container'></div>"


class Views.EditAttribute extends Backbone.View
    tagName: 'li'

    render: () ->
        @$el.html attribute_template @model.toHumanJSON()
        @rating = new UI.Rating
            el:    @$ 'div'
            field: 'rating'
            model: @model
            values: @options.values
            patch: true
        @rating.render()
        @


class Views.AttributeGroup extends Backbone.View
    options:
        ItemView: Views.EditAttribute

    render: () ->
        @$el.html @options.template {header: @options.header}
        @collection.each (item) ->
            view = new @options.ItemView
                model: item
                values: @options.values
            @$('.trait-list').append view.render().$el
        , @
        @
