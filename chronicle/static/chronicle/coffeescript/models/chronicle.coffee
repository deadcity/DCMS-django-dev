Models_NS = Tools.create_namespace 'Chronicle.Models'


class Models_NS.Chronicle extends Backbone.Model
    defaults:
        id      : null
        enabled : false

        name        : null
        description : null

    parse: (raw) ->
        {
            id      : parseInt raw.id, 10
            enabled : raw.enabled

            name        : raw.name
            description : raw.description
        }

    url: () ->
        "/api/chronicle/Chronicle/#{ if @id? then "#{@id}/" else '' }"

    toHumanJSON: () ->
        @toJSON()
