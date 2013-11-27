Tools.create_namespace 'Table'
Tools.create_namespace 'Table.Enums'
Tools.create_namespace 'Table.Models'
Tools.create_namespace 'Table.Views'


Table.Enums.RecordState = RecordState = new Tools.Enum [
    { name: 'UNDEF',           }
    { name: 'CLEAN',           }
    { name: 'DELETED',         }
    { name: 'PENDING_NEW',     }
    { name: 'PENDING_UPDATE',  }
    { name: 'PENDING_DELETE',  }
    { name: 'PENDING_RESTORE', }
]

replicated_states = [
    RecordState.CLEAN,
    RecordState.PENDING_UPDATE,
    RecordState.PENDING_DELETE
]

editing_states = [
    RecordState.PENDING_NEW,
    RecordState.PENDING_UPDATE,
    RecordState.PENDING_RESTORE
]


Table.Enums.EditState = EditState = new Tools.Enum [
    { name: 'UNCHANGED', }
    { name: 'VALID',     }
    { name: 'INVALID',   }
]


###
  A presentation model for the row-view InplaceEdit below.  The record model
  must trigger valid/invalid events.
###

class Table.Models.InplacePresentation extends Table.Models.RowPresentation
    defaults:
        # record_state   : RecordState.CLEAN
        edit_state     : EditState.UNCHANGED
        record_changed : false
        # override 'selected' option

    initialize: (attributes, options) ->
        super
        options = options ? {}

        @record.isNew = () =>
            return not _.contains replicated_states, @get_record_state()

        @invalid_attributes = {}
        @listenTo @record, 'invalid', @on_invalid
        @listenTo @record, 'valid',   @on_valid

        @on_record_sync @record
        @listenTo @record, 'sync', @on_record_sync

    get_record_state: () ->
        return @record.collection.record_state

    should_hide: () ->
        return  @get_record_state() is RecordState.DELETED

    toJSON: (options) ->
        attr = super
        attr.record_state = @get_record_state()
        return attr

    on_record_sync: (model, resp, options) ->
        @set 'record_changed', false
        @record.once 'change', (model, options) => @set 'record_changed', true

    on_invalid: (model, attributes, options) ->
        for field, value of attributes
            @invalid_attributes[field] = value

        @set 'edit_state', EditState.INVALID

    on_valid: (model, attributes, options) ->
        for field, value of attributes
            delete @invalid_attributes[field]

        if not options.xhr? and _.keys(@invalid_attributes).length == 0
            @set 'edit_state', if @get 'record_changed' then EditState.VALID else EditState.UNCHANGED


###
  A view for a table row that switches between two modes, STATIC and EDIT.  The
  mode is determined by the model's 'record_state' field as per the table below.
  The record model must define a 'check_valid' function that triggers
  valid/invalid events.

           RecordState   |  Mode
        -----------------+--------
         CLEAN           | STATIC
         DELETED         | STATIC
         PENDING_NEW     | EDIT
         PENDING_UPDATE  | EDIT
         PENDING_DELETE  | EDIT
         PENDING_RESTORE | EDIT

  To use this view, you must extend it and specify the following properties.
    @prop static_template - The template for STATIC-mode.
    @prop edit_template   - The template for EDIT-mode.


  The templates should have the following components for the specified states:

    CLEAN
        @button edit    - Changes RecordState to PENDING_UPDATE.  Enables editing.
        @button delete  - Changes RecordState to PENDING_DELETE.
        @link   history - Goes to history for this record.

    DELETED
        @button restore - Changes RecordState to PENDING_RESTORE.  Enables editing.
        @link   history - Goes to history for this record.

    PENDING_NEW
        @button discard - Deletes model.  Removes row.

    PENDING_UPDATE
        @button discard - Changes RecordState to CLEAN.  Disables editing.
                          Restores field values from server.
        @button delete  - Changes RecordState to PENDING_DELETE.  Disables editing.
        @link   history - Goes to history for this record.

    PENDING_DELETE
        @button restore - Changes RecordState to PENDING_UPDATE.  Enables Editing.
        @link   history - Goes to history for this record.

    PENDING_RESTORE
        @button discard - Changes RecordState to DELETED.  Disables editing.
                          Restores field values from server.
        @link   history - Goes to history for this record.
###

class Table.Views.InplaceEdit extends Table.Views.Row
    options: _.extend({}, Table.Views.Row.prototype.options, {
        static_template: null
        edit_template: null
    })

    initialize: (options) ->
        super

        # When the record data changes, we only want to re-render the whole row
        # if that change did not come from the html controls.  Hence, we route
        # the 'change' event through the handler 'on_change_record'
        @stopListening @model.record, 'change', @render

        @listenTo @model.record, 'change',              @on_record_change
        @listenTo @model,        'change:edit_state',   @on_change_edit_state
        @listenTo @model.record, 'invalid',             @on_invalid
        @listenTo @model.record, 'valid',               @on_valid

    events: () ->
        'click button[name="edit"]'    : 'on_edit'
        'click button[name="delete"]'  : 'on_delete'
        'click button[name="discard"]' : 'on_discard'
        'click button[name="restore"]' : 'on_restore'

    render: () ->
        @undelegateEvents()
        template = if _.contains editing_states, @model.get_record_state() then @options.edit_template else @options.static_template
        @$el.html template @model.toJSON nest: true
        @delegateEvents()
        # if (@model.get_record_state()) isnt RecordState.CLEAN
        #     @model.record.check_valid()
        @_apply_record_state_class @model.get_record_state()
        @_apply_edit_state_class   @model.get 'edit_state'

        if (@model.get_record_state()) in editing_states
            @_check_input_validity()

        @

    _set_field: (field, el, options) ->
        options = _.extend
            source: @
            construct: (v) -> if v is '' then null else v
        , options ? {}

        if _.has options, 'construct'
            construct = options.construct
            delete options.construct
        else
            construct = null

        options.source = @
        attr = {}
        attr[field] = if construct? then construct el.value else el.value

        @model.record.set attr, options

    _apply_record_state_class: (record_state) ->
        classes = _.pluck RecordState._elements, 'name'
        @$el.removeClass classes.join ' '

        @$el.addClass record_state.name

    _apply_edit_state_class: (edit_state) ->
        classes = _.pluck EditState._elements, 'name'
        @$el.removeClass classes.join ' '

        switch edit_state
            when EditState.UNCHANGED
                if _.contains editing_states, @model.get_record_state()
                    @$el.addClass 'UNCHANGED'

            when EditState.VALID
                @$el.addClass 'VALID'

            when EditState.INVALID
                @$el.addClass 'INVALID'

    _check_input_validity: (options) ->
        if options?
            options = _.clone options
        else
            options = {}

        options.html_invalid = {}
        for el in @$ 'input, select, textarea'
            if el.checkValidity and not el.checkValidity()
                options.html_invalid[el.name] = el.value
        @model.record.check_valid null, options

    # This funtion is called when any fields of model.record change.
    on_record_change: (model, options) ->
        if options?
            options = _.clone options
        else
            options = {}

        @_check_input_validity options

        # Skip re-rendering if the model was changed by this view.
        if options.source is @
            return

        # # Skip re-rendering if the model was changed by
        # if $.contains @el, options.source
        #     return

        @render()

    # This function is called when 'record_state' of model changes.
    on_change_record_state: (model, value, options) ->
        @render()

    on_change_edit_state: (model, value, options) ->
        @_apply_edit_state_class value

    on_invalid: (model, attributes, options) ->
        for field, value of attributes
            control = @$ "[name='#{field}']"
            control.addClass 'invalid'

    on_valid: (model, attributes, options) ->
        for field, value of attributes
            control = @$ "[name='#{field}']"
            control.removeClass 'invalid'

    on_edit: () ->
        switch @model.get_record_state()
            when RecordState.CLEAN
                @model.record.trigger 'move_to', @model.record, RecordState.PENDING_UPDATE, source: @

    on_delete: () ->
        switch @model.get_record_state()
            when RecordState.CLEAN, RecordState.PENDING_UPDATE
                @model.record.trigger 'move_to', @model.record, RecordState.PENDING_DELETE, source: @

    on_discard: () ->
        switch @model.get_record_state()
            when RecordState.PENDING_NEW
                @model.record.destroy()
            when RecordState.PENDING_UPDATE
                @model.set
                    record_state : RecordState.CLEAN
                    edit_state   : EditState.UNCHANGED
                , source: @
                @model.record.fetch()
            when RecordState.PENDING_RESTORE
                @model.set
                    record_state : RecordState.DELETED
                    edit_state   : EditState.UNCHANGED
                , source: @
                @model.record.fetch()

    on_restore: () ->
        switch @model.get_record_state()
            when RecordState.DELETED
                @model.record.trigger 'move_to', @model.record, RecordState.PENDING_RESTORE, source: @
            when RecordState.PENDING_DELETE
                @model.record.trigger 'move_to', @model.record, RecordState.PENDING_UPDATE, source: @


class Table.InplaceEditTable extends Table.Table
    initialize: (options) ->
        buckets = {}
        for state in RecordState._elements
            bucket = new Backbone.Collection null,
                model: @collection.model
            bucket.record_state = state
            buckets[state.name] = bucket

        @collection = new Common.Collections.BucketCollection null,
            buckets: buckets
            assign_bucket: (model, options) -> @buckets[options.record_state.name]

        super

        @listenTo @collection, 'move_to', @on_move_to
        @listenTo @collection, 'move', @on_move_bucket

    on_move_to: (record, record_state, options) ->
        # TODO

    on_move_bucket: (record, src, dest, options) ->
        # TODO
