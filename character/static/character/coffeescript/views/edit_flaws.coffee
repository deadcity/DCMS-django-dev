Views = Tools.create_namespace 'Character.Views'


Traits.Models.Flaw.prototype.requires_modal = (attributes) ->
    attr = attributes ? @attributes

    if attr.requires_specification
        return true

    if attr.requires_description
        return true

    return false


flaw_template = _.template '<%= trait.name %><% if (trait.requires_specification) { %>: <%= specification %><% } %><% if (Traits.Models.Flaw.prototype.requires_modal(trait)) { %> <div class=\'edit\'>[edit]</div><% } %> <div class=\'remove\'>[X]</div>'


class Views.FlawModal extends Backbone.View
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


class Views.CharacterFlaw extends Backbone.View
    tagName: 'li'

    initialize: (options) ->
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'destroy', @remove
        @listenTo @model, 'change',  @render

    events:
        'click div.edit'   : 'edit_item'
        'click div.remove' : 'delete_item'

    render: () ->
        @$el.html flaw_template @model.toHumanJSON()
        @delegateEvents()
        @

    edit_item: () ->
        UI.create_modal
            View: Views.FlawModal
            view_options:
                template: @options.modal_template
                model: @model

    delete_item: () ->
        @model.destroy()


group_template  = _.template '<optgroup label=\'<%= name %>\'></optgroup>'
option_template = _.template '<option value=\'<%= id %>\'><%= name %></option>'


class Views.FlawSection extends Backbone.View
    options:
        ItemView: Views.CharacterFlaw
        ModalView: Views.FlawModal
        modal_template: null

    initialize: (options) ->
        @listenTo @collection, 'add', @render_flaw

    events:
        'click button[name=\'add\']' : 'add_flaw'

    render: () ->
        @$el.html @options.template()
        @collection.each (item) ->
            @render_flaw item
        , @

        grouped = Traits.Objects.Flaw.groupBy 'type'
        _.each Traits.Enums.FlawType._elements, (type) ->
            group_element = $ group_template type
            flaw_list = _.sortBy grouped[type], (item) -> item.get 'name'
            _.each flaw_list, (item) ->
                group_element.append option_template item.toHumanJSON()
            @$('select').append group_element
        @

    render_flaw: (model) ->
        view = new @options.ItemView
            model: model
            modal_template: @options.modal_template
        @$('.trait-list').append view.render().$el

    add_flaw: () ->
        model = new @collection.model()
        trait = Traits.Objects.Flaw.get @$('select[name=\'flaw\']').val()
        model.set
            character : Character.Objects.Character.id
            trait     : trait

        model.save()
        @collection.add model

        if trait.requires_modal()
            UI.create_modal
                View: Views.FlawModal
                view_options:
                    template: @options.modal_template
                    model: model
