Views = Tools.create_namespace 'Character.Views'


power_template = _.template '<%= trait.group %> <%= trait.rating %>: <%= trait.name %><div class=\'remove\'>[X]</div>'


class Views.CharacterPower extends Backbone.View
    tagName: 'li'

    initialize: (options) ->
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'destroy', @remove

    events:
        'click div.remove': 'delete_item'

    render: () ->
        @$el.html power_template @model.toHumanJSON()
        @delegateEvents()
        @

    delete_item: () ->
        @model.destroy()


group_template  = _.template '<optgroup label=\'<%= group %>\'></optgroup>'
option_template = _.template '<option value=\'<%= id %>\'><%= rating %>: <%= name %></option>'


class Views.PowerSection extends Backbone.View
    options:
        ItemView: Views.CharacterPower

    initialize: (options) ->
        @listenTo @collection, 'add', @render_character_power

    events:
        'click button[name=\'add\']': 'add_power'

    render: () ->
        @$el.html @options.template()
        @collection.each (item) ->
            @render_character_power item
        , @

        grouped = Traits.Objects.Power.groupBy 'group'
        keys = _.keys grouped
        keys.sort()
        _.each keys, (group) ->
            group_element = $ group_template group: group
            grouped[group].sort (a, b) ->
                a_rating = a.get 'rating'
                b_rating = b.get 'rating'
                if a_rating < b_rating
                    return -1
                else if a_rating > b_rating
                    return 1

                a_name = a.get('name')
                b_name = b.get('name')
                if a_name < b_name
                    return -1
                else if a_name > b_name
                    return 1
                return 0
            _.each grouped[group], (item) ->
                group_element.append option_template item.toHumanJSON()
            @$('select[name=\'power\']').append group_element
        @

    render_character_power: (model) ->
        view = new @options.ItemView
            model: model
        @$('.trait-list').append view.render().$el
        view

    add_power: () ->
        model = new @collection.model()
        model.set
            character : Character.Objects.Character.id
            trait     : Traits.Objects.Power.get @$('select[name=\'power\']').val()

        model.save()
        @collection.add model
