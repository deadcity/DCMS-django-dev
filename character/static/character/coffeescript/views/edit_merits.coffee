Views = Tools.create_namespace 'Character.Views'


Traits.Models.Merit.prototype.requires_modal = (attributes) ->
    attr = attributes ? @attributes

    if attr.allowed_ratings.length > 1
        return true

    if attr.requires_specification
        return true

    if attr.requires_description
        return true

    return false


merit_template = _.template '<%= trait.name %> (<%= rating %>)<% if (trait.requires_specification) { %>: <%= specification %><% } %><% if (Traits.Models.Merit.prototype.requires_modal(trait)) { %> <div class=\'edit\'>[edit]</div><% } %> <div class=\'remove\'>[X]</div>'


class Views.MeritModal extends Backbone.View
    className: 'modal-window'

    events:
        'keyup  input[name=\'specification\']'  : 'update_specification'
        'change input[name=\'specification\']'  : 'save_specification'
        'change textarea[name=\'description\']' : 'save_description'
        'click  button[name=\'close\']'         : 'close'

    render: () ->
        @$el.html @options.template @model.toHumanJSON()
        @rating = new UI.Rating
            el: @$ '.rating-container'
            model: @model
            values: @model.get('trait').get 'allowed_ratings'
            patch: true
        @rating.render()
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


class Views.CharacterMerit extends Backbone.View
    tagName: 'li'

    initialize: (options) ->
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'destroy', @remove
        @listenTo @model, 'change',  @render

    events:
        'click div.edit'   : 'edit_item'
        'click div.remove' : 'delete_item'

    render: () ->
        @$el.html merit_template @model.toHumanJSON()
        @delegateEvents()
        @

    edit_item: () ->
        UI.create_modal
            View: Views.MeritModal
            view_options:
                template: @options.modal_template
                model: @model

    delete_item: () ->
        @model.destroy()


group_template  = _.template '<optgroup label=\'<%= name %>\'></optgroup>'
option_template = _.template '<option value=\'<%= id %>\'><%= name %></option>'


class Views.MeritSection extends Backbone.View
    options:
        ItemView: Views.CharacterMerit
        ModalView: Views.MeritModal
        modal_template: null

    initialize: (options) ->
        @listenTo @collection, 'add', @render_merit

    events:
        'click button[name=\'add\']' : 'add_merit'

    render: () ->
        @$el.html @options.template()
        @collection.each (item) ->
            @render_merit item
        , @

        grouped = Traits.Objects.Merit.groupBy 'type'
        _.each Traits.Enums.MeritType._elements, (type) ->
            group_element = $ group_template type
            merit_list = _.sortBy grouped[type], (item) -> item.get 'name'
            _.each merit_list, (item) ->
                group_element.append option_template item.toHumanJSON()
            @$('select').append group_element
        @

    render_merit: (model) ->
        view = new @options.ItemView
            model: model
            modal_template: @options.modal_template
        @$('.trait-list').append view.render().$el

    add_merit: () ->
        model = new @collection.model()
        trait = Traits.Objects.Merit.get @$('select[name=\'merit\']').val()
        model.set
            character : Character.Objects.Character.id
            trait     : trait
            rating    : trait.get('allowed_ratings')[0]

        model.save()
        @collection.add model

        if trait.requires_modal()
            UI.create_modal
                View: Views.MeritModal
                view_options:
                    template: @options.modal_template
                    model: model
