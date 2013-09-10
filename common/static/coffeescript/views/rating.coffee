Rating_NS = Tools.create_namespace 'Rating'


class ItemPresentation extends Backbone.Model
    defaults:
        value:      null
        selected:   false
        selecting:  false
        selectable: false

class CircleView extends SVGTools.SVGView
    tagName: 'circle',

    initialize: (options) ->
        @listenTo @model, 'change:selected',   (model) -> @set_class 'selected',  model.get 'selected'
        @listenTo @model, 'change:selecting',  (model) -> @set_class 'selecting', model.get 'selecting'
        @listenTo @model, 'change:selectable', (model) -> @delegateEvents()

    events: () ->
        if @model.get 'selectable'
            return {
                'mouseover' : 'hover'
                'mouseout'  : 'unhover'
                'mousedown' : 'mousedown'
                'mouseup'   : 'mouseup'
            }
        {}

    # Propagate DOM events through the presentation-model.
    hover:     () -> @model.trigger 'hover',     @model
    unhover:   () -> @model.trigger 'unhover',   @model
    mousedown: () -> @model.trigger 'mousedown', @model
    mouseup:   () -> @model.trigger 'mouseup',   @model

    render: () ->
        @$el.attr('cx', @options.r / 2)
            .attr('cy', (@model.get('index') - @options.min + .5) * @options.r)
            .attr('r',  @options.r)

        if @model.get 'selected'  then @$el.addClass 'selected'
        if @model.get 'selecting' then @$el.addClass 'selecting'

        @delegateEvents()
        @

    set_class: (name, value) ->
        if value then @$el.addClass name else @$el.removeClass name


class Rating_NS.Rating extends SVGTools.SVGView
    tagName: 'svg'

    options:
        min: 1
        max: 5
        inc: 1

        r: 10

        field: 'rating'
        View: CircleView

    initialize: (options) ->
        @collection = new Backbone.Collection null, {model: ItemPresentation}
        for i in [@options.min .. @otions.max]
            @collection.add {
                value: i
                index: i
                selectable: i % @options.inc == true
            }

        @listenTo @model 'change:' + @options.field, @on_change_rating
        @listenTo @collection, 'hover',     @on_hover
        @listenTo @collection, 'unhover',   @on_unhover
        @listenTo @collection, 'mousedown', @on_mousedown
        @listenTo @collection, 'mouseup',   @on_mouseup

        @on_change_rating @model

    on_change_rating: (model, options) ->
        val = model.get @options.field
        @collection.each (item) ->
            item.set 'selected', val >= item.get 'value'

    render: () ->
        @$el.empty()

        @collection.each (item) ->
            view = new @options.View _.extend {}, @options, {model: item}
            view.render()
            @$el.append view.el
        , @

        @

    on_hover: (model) ->
        val = model.get 'value'
        @collection.each (m) ->
            m.set 'selecting', val >= m.get 'value'

    on_unhover: (model) ->
        @collection.each (m) ->
            m.set 'selecting', false

    on_mousedown: (model) ->

    on_mouseup: (model) ->
        @collection.each (m) ->
            if m isnt model
                m.set 'selected', false
        model.set 'selected', true
        @model.set @options.field, model.get 'value'
