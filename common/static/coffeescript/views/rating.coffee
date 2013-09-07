Rating_NS = Tools.create_namespace 'Rating'


class ItemPresentation extends Backbone.Model
    defaults:
        value:      null
        selected:   false
        selecting:  false
        selectable: false

class CircleView extends SVGTools.SVGView
    tagName: 'svg',

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
        @$el.empty()

        item = @make 'circle',
            cx : @options.r
            cy : @options.r
            r  : @options.r
        $item = $ item

        if @model.get('value') is 0
            # inner circle
            item = @make 'circle',
                cx : @options.r
                cy : @options.r
                r  : @options.r / 2
            $(item).addClass 'zero-marker'
            @$el.append item
            $item.addClass 'zero-selecting'

        else
            $item.addClass 'rating-value'

        if @model.get 'selected'  then $item.addClass 'selected'
        if @model.get 'selecting' then $item.addClass 'selecting'
        @$el.append $item
        @$item = $item
        @$el.width  @options.r * 2
        @$el.height @options.r * 2

        @delegateEvents()
        @

    set_class: (name, value) ->
        if value then @$item.addClass name else @$item.removeClass name


class Rating_NS.Rating extends Backbone.View
    options:
        values: null
        r: 5

        field: 'rating'
        View: CircleView
        patch: false

    initialize: (options) ->
        @collection = new Backbone.Collection null, {model: ItemPresentation}
        val = @model.get @options.field

        min = if _.contains @options.values, 0 then 0 else 1

        for i in [min .. _.max @options.values]
            @collection.add
                value: i
                selected: i <= val
                selectable: _.contains @options.values, i

        @listenTo @model, 'change:' + @options.field, @on_change_rating
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
            view = new @options.View _.extend {}, @options,
                model: item
                el: null
            view.render()
            @$el.append view.$el
        , @

        @

    on_hover: (model) ->
        val = model.get 'value'
        if val is 0
            zero_marker = @collection.find (m) ->
                0 is m.get 'value'
            zero_marker.set 'selecting', true

        else
            @collection.each (m) ->
                m_val = m.get 'value'
                if m_val isnt 0
                    m.set 'selecting', val >= m_val

    on_unhover: (model) ->
        @collection.each (m) ->
            m.set 'selecting', false

    on_mousedown: (model) ->

    on_mouseup: (model) ->
        value = model.get 'value'
        @collection.each (m) ->
            m.set 'selected', value >= m.get 'value'

        attr = {}
        attr[@options.field] = value
        if value is @model.get @options.field
            return

        if @options.patch
            @model.save attr, patch: true
        else
            @model.set attr
