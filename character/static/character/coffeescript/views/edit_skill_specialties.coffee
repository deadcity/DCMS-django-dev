Views = Tools.create_namespace 'Character.Views'


specialty_template = _.template '<span class=\'specialty-label\'><%= trait.name %></span>: <%= specialty %><div class=\'remove\'>✖</div>'


class Views.SkillSpecialty extends Backbone.View
    tagName: 'li'

    initialize: (options) ->
        @listenTo @model, 'remove',  @remove
        @listenTo @model, 'destory', @remove

    events:
        'click div.remove': 'delete_item'

    render: () ->
        @$el.html specialty_template @model.toHumanJSON()
        @delegateEvents()
        @

    delete_item: () ->
        @model.destroy()


group_template  = _.template '<optgroup label=\'<%= name %>\'></optgroup>'
option_template = _.template '<option value=\'<%= id %>\'><%= name %></option>'


class Views.SkillSpecialtySection extends Backbone.View
    options:
        ItemView: Views.SkillSpecialty

    initialize: (options) ->
        @listenTo @collection, 'add', @render_specialty

    events:
        'click button[name=\'add\']': 'add_specialty'

    render: () ->
        @$el.html @options.template()
        @collection.each (item) ->
            @render_specialty item
        , @

        grouped = Traits.Objects.Skill.groupBy 'type'
        _.each Traits.Enums.SkillType._elements, (type) ->
            group_element = $ group_template type
            skill_list = _.sortBy grouped[type], (item) -> item.get 'name'
            _.each skill_list, (item) ->
                group_element.append option_template item.toHumanJSON()
            @$('select').append group_element
        @

    render_specialty: (model) ->
        view = new @options.ItemView
            model: model
        @$('.trait-list').append view.render().$el
        view

    add_specialty: () ->
        model = new @collection.model()
        model.set
            character : Character.Objects.Character.id
            trait     : Traits.Objects.Skill.get @$('select[name=\'skill\']').val()
            specialty : @$('[name=\'specialty\']').val()

        model.save()
        @collection.add model
