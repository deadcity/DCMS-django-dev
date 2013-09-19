UI = Tools.create_namespace 'UI'


class UI.Overlay extends Backbone.View
    id: 'overlay'

    options:
        color      : '#606060'
        opacity    : 0.8
        load_speed : 200

    render: () ->
        page = $ 'body'
        page.append @$el

        @$el.css
            position   : 'fixed'
            left       : '0px'
            top        : '0px'
            width      : '100%'
            height     : '100%'
            'z-index'  : '1000'
            background : @options.color
            opacity    : 0

        @$el.fadeTo @options.load_speed, @options.opacity

        @

    close: () ->
        @$el.fadeTo @options.load_speed, 0, () => @remove()



UI.create_modal = (options) ->
    view = new options.View options.view_options
    overlay = new UI.Overlay options.overlay_options
    overlay.listenTo view, 'close', overlay.close
    overlay.render()
    $('body').append view.render().$el
