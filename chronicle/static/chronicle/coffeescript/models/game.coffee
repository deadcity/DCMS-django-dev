Models_NS = Tools.create_namespace 'Chronicle.Models'


class Models_NS.Game extends Backbone.Model
    defaults:
        id      : null
        enabled : false

        name : null
        date : null

    parse: (raw) ->
        {
            id      : parseInt raw.id, 10
            enabled : raw.enabled

            name : raw.name
            date : if raw.date? then new Date raw.date else null
        }

    url: () ->
        "/api/chronicle/Game/#{ if @id? then "#{@id}/" else '' }"

    toJSON: () ->
        attr = _.clone @attributes

        attr.date = attr.date?.toISOString()

    toHumanJSON: () ->
        @toJSON()
