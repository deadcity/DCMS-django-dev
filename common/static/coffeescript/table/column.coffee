Enums  = Tools.create_namespace 'Table.Enums'
Models = Tools.create_namespace 'Table.Models'
Views  = Tools.create_namespace 'Table.Views'

SORT_DIRECTION = Enums.SORT_DIRECTION = new Tools.Enum [
    { name: 'UNSORTED',   symbol: '', },
    { name: 'ASCENDING',  symbol: ' ▲', },
    { name: 'DESCENDING', symbol: ' ▼', },
]


###
  A view to manage a column's header.  Click the header to sort by that field.

  @prop model - the column presentation model for this column
###

class Views.Header extends Backbone.View
    tagName: 'th'
    template: _.template '<%= header %>' +
        "<% if (sort_func) { %><span class='table-sort-indicator'><%= sort_direction.symbol %></span><% } %>"

    initialize: (options) ->
        @listenTo @model, 'destroy', @remove
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'change',  @render

    events:
        'click' : 'on_click'

    render: () ->
        @$el.html @template @model.toJSON()
        if @model.has 'sort_func'
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
  @attr sort_func      - function used to extract a sortable value from fields
  @attr sort_direction - enumeration used interally for sorting
                         default: Table.Enums.SORT_DIRECTION.UNSORTED
###

class Models.ColumnPresentation extends Backbone.Model
    defaults:
        header: null
        field:  null

        sort_func:      undefined
        sort_direction: SORT_DIRECTION.UNSORTED

    initialize: (attributes, options) ->
        if attributes.sort_func is undefined
            @set 'sort_func', (field) -> field ? ''
        @HeaderView = options?.HeaderView ? Views.Header
        @on 'change:sort_direction', @sort_cascade, @

    sort_cascade: () ->
        if not @has 'sort_func' then return

        sort_direction = @get 'sort_direction'
        if sort_direction is SORT_DIRECTION.UNSORTED
            @trigger 'sort:unset', @, sort_direction
        else
            @trigger 'sort:set',   @, sort_direction

    cycle_sort: () ->
        if not @has 'sort_func' then return

        switch @get 'sort_direction'
            when SORT_DIRECTION.UNSORTED   then @set 'sort_direction', SORT_DIRECTION.ASCENDING
            when SORT_DIRECTION.ASCENDING  then @set 'sort_direction', SORT_DIRECTION.DESCENDING
            when SORT_DIRECTION.DESCENDING then @set 'sort_direction', SORT_DIRECTION.ASCENDING
