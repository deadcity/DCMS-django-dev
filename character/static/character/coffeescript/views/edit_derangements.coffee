Views = Tools.create_namespace 'Character.Views'


Traits.Models.Derangement.prototype.requires_modal = (attributes) ->
    attr = attributes ? @attributes

    if attr.requires_specification
        return true

    if attr.requires_description
        return true

    return false


derangement_template = _.template '<%= trait.name %><% if (trait.requires_specification) { %>: <%= specification %><% } %><% if (Traits.Models.Derangement.prototype.requires_modal(trait)) { %> <div class=\'edit\'>[edit]</div><% } %> <div class=\'remove\'>[X]</div>'


class Views.DerangementModal extends Backbone.View
    className: 'modal-window'

    events:
        'keyup  input[name=\'specification\']'  : 'update_specification'
        'change input[name=\'specification\']'  : 'save_specification'
        'change textarea[name=\'description\']' : 'save_description'
        'click  button[name=\'close\']'         : 'close'

    render: () ->
        @$el.html @options.template @model.toHumanJSON()
        @delegateEvents()
        @

    _change_field: (e, field, construct) ->
        attr = {}
        attr[field] = if e.target.value is '' then null else construct e.target.value

        @model.save attr, { patch: true }

    update_specification: (e) ->
        span = @$ 'span[name=\'specification\']'
        span.html e.target.value

    save_specification: (e) ->
        @_change_field e, 'specification', (v) -> v

    save_description: (e) ->
        @_change_field e, 'description', (v) -> v

    close: () ->
        @remove()
        @trigger 'close'


class Views.CharacterDerangement extends Backbone.View
    tagName: 'li'

    initialize: (options) ->
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'destroy', @remove
        @listenTo @model, 'change',  @render

    events:
        'click div.edit'   : 'edit_item'
        'click div.remove' : 'delete_item'

    render: () ->
        @$el.html derangement_template @model.toHumanJSON()
        @delegateEvents()
        @

    edit_item: () ->
        UI.create_modal
            View: Views.DerangementModal
            view_options:
                template: @options.modal_template
                model: @model

    delete_item: () ->
        @model.destroy()


group_template  = _.template '<optgroup label=\'<%= name %>\'></optgroup>'
option_template = _.template '<option value=\'<%= id %>\'><%= name %></option>'


class Views.DerangementSection extends Backbone.View
    options:
        ItemView: Views.CharacterDerangement
        ModalView: Views.DerangementModal
        modal_template: null

    initialize: (options) ->
        @listenTo @collection, 'add', @render_derangement

    events:
        'click button[name=\'add\']' : 'add_derangement'

    render: () ->
        @$el.html @options.template()
        @collection.each (item) ->
            @render_derangement item
        , @

        grouped = Traits.Objects.Derangement.groupBy 'type'
        _.each Traits.Enums.DerangementType._elements, (type) ->
            group_element = $ group_template type
            derangement_list = _.sortBy grouped[type], (item) -> item.get 'name'
            _.each derangement_list, (item) ->
                group_element.append option_template item.toHumanJSON()
            @$('select').append group_element
        @

    render_derangement: (model) ->
        view = new @options.ItemView
            model: model
            modal_template: @options.modal_template
        @$('.trait-list').append view.render().$el

    add_derangement: () ->
        model = new @collection.model()
        trait = Traits.Objects.Derangement.get @$('select[name=\'derangement\']').val()
        model.set
            character : Character.Objects.Character.id
            trait     : trait

        model.save()
        @collection.add model

        if trait.requires_modal()
            UI.create_modal
                View: Views.DerangementModal
                view_options:
                    template: @options.modal_template
                    model: model
