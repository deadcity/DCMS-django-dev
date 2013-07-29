Table_NS = Tools.create_namespace 'Table'

SORT_DIRECTION = Table.Enum.SORT_DIRECTION


###
  @prop columns    - backbone collection for column-presentation models
  @prop all_rows   - backbone collection for all row-presentation models
  @prop rows       - backbone collection for only row-presentation models that are displayed
  @prop collection - backbone collection for domain models
###

class Table_NS.Table extends Backbone.View
    tagName: 'table'

    template: _.template '<thead><tr></tr></thead><tbody></tbody>'

    ###
      @brief Initialize the table view.
      @arg ColumnPresentation - class to use for the column presentation model
                                default: Table.Models.ColumnPresentation
      @arg RowPresentation    - class to use for the row presentation model
                                default: Table.Models.RowPresentation
      @arg RowView            - class to use for the row view
                                default: Table.Views.Row
      @arg row_template       - callable to generate html for a row
                                this will override RowView.prototype.template
      @arg filter             - function to filter presentation models by
    ###
    initialize: (options) ->
        options = options ? {}

        # default options
        @ColumnPresentation = options.ColumnPresentation ? Table_NS.Models.ColumnPresentation
        @RowPresentation    = options.RowPresentation    ? Table_NS.Models.RowPresentation
        @RowView            = options.RowView            ? Table_NS.Views.Row
        @_filter            = options.filter
        @row_template       = options.row_template

        if options.columns instanceof Backbone.Collection
            @columns = options.columns
        else
            @columns = new Backbone.Collection options.columns, {model: @ColumnPresentation}

        @all_rows = new Backbone.Collection null, {model: @RowPresentation}
        @rows     = new Backbone.Collection null, {model: @RowPresentation}

        @collection.each @on_add_record, @
        @listenTo @collection, 'add', @on_add_record

        @listenTo @columns,    'sort:set', @sort
        @listenTo @rows,       'remove',   @hide_row
        @listenTo @rows,       'add',      @render_row
        @listenTo @all_rows,   'change',   @filter_pres_model

    render: () ->
        @rows.each @hide_row, @
        @$el.empty()
        @$el.html @template @model?.toJSON()

        @render_header()
        @rows.each @render_row, @

        @

    render_header: () ->
        header = @$ 'thead tr'
        header.empty()
        @columns.each (column) ->
            view = new column.HeaderView {model: column}
            header.append view.render().el

    render_row: (model) ->
        view = new @RowView {model: model, template: @row_template}
        view.listenTo model, 'hide', view.remove
        model.once 'destroy', () ->
            view.stopListening model
        view.render().move_to @$('tbody'), @rows.indexOf(model), @

    hide_row: (model, collection) ->
        model.trigger 'hide', model, collection

    filter: (fltr) ->
        @_filter = fltr

        rows = if @_filter? then @all_rows.filter @_filter else @all_rows.models
        @rows.set rows, {merge: false}

    filter_pres_model: (model) ->
        if not @_filter? or @_filter model
            @rows.add model
        else
            @rows.remove model

    sort: (column, direction) ->
        @columns.each (col) ->
            if col isnt column
                col.set 'sort_direction', SORT_DIRECTION.UNSORTED

        @collection.off 'change',    @rows.sort, @rows
        @stopListening  @collection, 'change',   @sync_row_order

        if not column?
            return

        field = column.get 'field'
        comp = (a, b) ->
            a_ = a.record.get field
            b_ = b.record.get field
            if a_ <  b_ then return -1
            if a_ == b_ then return 0
            return 1

        switch direction
            when SORT_DIRECTION.UNSORTED   then @rows.comparator = undefined; return
            when SORT_DIRECTION.ASCENDING  then @rows.comparator = comp
            when SORT_DIRECTION.DESCENDING then @rows.comparator = (a, b) -> comp b, a

        @rows.sort()
        @collection.on 'change',    @rows.sort, @rows
        @listenTo      @collection, 'change',   @sync_row_order

        @sync_row_order()

    sync_row_order: () ->
        tbody = @$ 'tbody'
        @rows.each (row_pres, idx) ->
            row_pres.trigger 'command:move_to', tbody, idx, @
        , @

    on_add_record: (model, collection, options) ->
        pres_model = new @RowPresentation null, _.extend {record: model}, options
        @all_rows.add pres_model
        @filter_pres_model pres_model

        pres_model.on 'change', @filter_pres_model, @
        pres_model.record.on 'change', () ->
            @filter_pres_model pres_model
        , @
