Enum_NS   = Tools.create_namespace 'Table.Enum'
Models_NS = Tools.create_namespace 'Table.Models'
Views_NS  = Tools.create_namespace 'Table.Views'

SORT_DIRECTION = Enum_NS.SORT_DIRECTION = new Enum.Enum [
    { name: 'UNSORTED',   symbol: '', },
    { name: 'ASCENDING',  symbol: ' ▲', },
    { name: 'DESCENDING', symbol: ' ▼', },
]


###
  A view to manage a column's header.  Click the header to sort by that field.

  @prop model - the column presentation model for this column
###

class Views_NS.Header extends Backbone.View
    tagName: 'th'
    template: _.template '<%= header %>' +
        "<span class='table-sort-indicator'><%= sort_direction.symbol %></span>"

    initialize: (options) ->
        @listenTo @model, 'destroy', @remove
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'change',  @render

    events:
        'click' : 'on_click'

    render: () ->
        @$el.html @template @model.toJSON()
        if @model.get 'sortable'
            @$el.addClass 'sortable'
        else
            @$el.removeClass 'sortable'

        @delegateEvents()
        @

    on_click: () ->
        @model.cycle_sort()


###
  The default column presentation model.  Facilitates sorting.

  @attr header         - text displayed as the column's header
  @attr field          - attribute name in the domain model this column corresponds to
  @attr sort_direction - enumeration used interally for sorting
                         default: Table.Enum.SORT_DIRECTION.UNSORTED
###

class Models_NS.ColumnPresentation extends Backbone.Model
    defaults:
        header: null
        field:  null

        sortable:       true
        sort_direction: SORT_DIRECTION.UNSORTED

    initialize: (attributes, options) ->
        @HeaderView = options?.HeaderView ? Views_NS.Header
        @on 'change:sort_direction', @sort_cascade, @

    sort_cascade: () ->
        if not @get 'sortable' then return

        sort_direction = @get 'sort_direction'
        if sort_direction is SORT_DIRECTION.UNSORTED
            @trigger 'sort:unset', @, sort_direction
        else
            @trigger 'sort:set',   @, sort_direction

    cycle_sort: () ->
        if not @get 'sortable' then return

        switch @get 'sort_direction'
            when SORT_DIRECTION.UNSORTED   then @set 'sort_direction', SORT_DIRECTION.ASCENDING
            when SORT_DIRECTION.ASCENDING  then @set 'sort_direction', SORT_DIRECTION.DESCENDING
            when SORT_DIRECTION.DESCENDING then @set 'sort_direction', SORT_DIRECTION.ASCENDING
