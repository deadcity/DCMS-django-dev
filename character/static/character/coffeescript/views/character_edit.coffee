Views = Tools.create_namespace 'Character.Views'


Traits.Models.Merit.prototype.requires_modal = (attributes) ->
    attr = attributes ? @attributes

    if attr.allowed_ratings.length > 1
        return true

    return attr.requires_specification or attr.requires_description


Traits.Models.Flaw.prototype.requires_modal = (attributes) ->
    attr = attributes ? @attributes

    return attr.requires_specification or attr.requires_description


Traits.Models.Derangement.prototype.requires_modal = Traits.Models.Flaw.prototype.requires_modal


class Views.RatingControl extends Backbone.View
    render: () ->
        @$el.html @options.template @model.toHumanJSON()
        @rating = new UI.Rating
            el     : @$ 'div'
            field  : 'rating'
            model  : @model
            values : @options.values
            patch  : true
        @rating.render()
        @


class Views.TraitModal extends Common.Views.Control
    className: 'modal-window'

    events:
        'keyup  [name=\'specification\']' : 'update_specification'
        'change [name=\'specification\']' : 'save_specification'
        'change [name=\'description\']'   : 'save_description'
        'click  [name=\'close\']'         : 'close'

    render: (model, options) ->
        if options?.source is @
            return @

        super

        trait = @model.get 'trait'
        if trait.has 'allowed_ratings'
            @rating = new UI.Rating
                el: @$ '.rating-container'
                model: @model
                values: trait.get 'allowed_ratings'
                patch: true
            @rating.render()

        @

    update_specification: (e) ->
        span = @$ 'span[name=\'specification\']'
        span.html e.target.value

    save_specification: (e) ->
        @_change_field 'specification', e.target.value

    save_description: (e) ->
        @_change_field 'description', e.target.value

    close: () ->
        @remove()
        @trigger 'close'


class Views.EditableItem extends Common.Views.Item
    options: _.extend({}, Common.Views.Item.prototype.options, {
        ModalView     : null
        modal_options : null
    })

    events: () ->
        _.extend({}, super, {
            'click .edit' : 'edit_item'
        })

    edit_item: () ->
        modal_options = _.extend { model: @model }, @options.modal_options
        UI.create_modal
            View         : @options.ModalView
            view_options : modal_options


class Views.NumberTraitItem extends Common.Views.Control
    events:
        'change [name=\'rating\']' : 'save_rating'

    save_rating: (e) ->
        @_change_field 'rating', e.target.value, { construct: @_constructors.int }


class Views.CharacterTextItem extends Common.Views.Control
    events:
        'change textarea' : 'save_text'

    save_text: (e) ->
        @_change_field 'text', e.target.value


class Views.SkillSpecialtySection extends Common.Views.ListSelection
    initialize: (options) ->
        super
        @traits = Traits.Objects.Skill
        @options.groups = []

        groups = _.pairs @traits.groupBy 'type'
        _.each groups, (pair) =>
            @options.groups[pair[0]] = _.sortBy pair[1], (item) -> item.get 'name'

    add_item: () ->
        model = new @collection.model()
        model.set
            character : Character.Objects.Character.id
            trait     : @traits.get @$('select').val()
            specialty : @$('[name=\'specialty\']').val()

        model.save()
        @collection.add model


class Views.PowerSection extends Common.Views.ListSelection
    options: _.extend({}, Common.Views.ListSelection.prototype.options, {
        option_template: _.template '<option value=\'<%= id %>\'><%= rating %> - <%= name %></option>'
    })

    initialize: (options) ->
        super
        @traits = Traits.Objects.Power
        @options.groups = []

        groups = _.pairs @traits.groupBy 'group'
        _.each groups, (pair) =>
            @options.groups[pair[0]] = _.sortBy pair[1], (item) -> item.get('rating') + item.get('name')

    add_item: () ->
        model = new @collection.model()
        model.set
            character : Character.Objects.Character.id
            trait     : @traits.get @$('select').val()

        model.save()
        @collection.add model


class Views.MeritSection extends Common.Views.ListSelection
    initialize: (options) ->
        super
        @traits = Traits.Objects.Merit
        @options.groups = []
        @options.item_options = _.extend
            ModalView     : @options.ModalView
            modal_options : @options.modal_options
        , @options.item_options

        groups = _.pairs @traits.groupBy 'type'
        _.each groups, (pair) =>
            @options.groups[pair[0]] = _.sortBy pair[1], (item) -> item.get 'name'

    render_item: (model, collection, options) ->
        view = super
        trait = view.model.get 'trait'
        if collection is @collection and trait.requires_modal()
            view.edit_item()

    add_item: () ->
        model = new @collection.model()
        trait = @traits.get @$('select').val()
        model.set
            character : Character.Objects.Character.id
            trait     : trait
            rating    : trait.get('allowed_ratings')[0]

        model.save()
        @collection.add model


class Views.FlawSection extends Common.Views.ListSelection
    options: _.extend
        traits: null
    , Common.Views.ListSelection.prototype.options

    initialize: (options) ->
        super
        @options.groups = []
        @options.item_options = _.extend
            ModalView     : @options.ModalView
            modal_options : @options.modal_options
        , @options.item_options

        groups = _.pairs @options.traits.groupBy 'type'
        _.each groups, (pair) =>
            @options.groups[pair[0]] = _.sortBy pair[1], (item) -> item.get 'name'

    render_item: (model, collection, options) ->
        view = super
        trait = view.model.get 'trait'
        if collection is @collection and trait.requires_modal()
            view.edit_item()

    add_item: () ->
        model = new @collection.model()
        trait = @options.traits.get @$('select').val()
        model.set
            character : Character.Objects.Character.id
            trait     : trait

        model.save()
        @collection.add model
