###
  @file  base_model.coffee
  @brief Base model class for Models in coffeescript.
###


Tools.create_namespace 'ORM'


class ORM.BaseModel extends BackboneRelations.Model
    ## Destroy this object on the client only. (No effect on the server.)
    #
    #  This is basically the exact same implementation as Backbone.Model's
    #  destroy(options) except that it doesn't sync with the server.  It will
    #  trigger the 'dismantle' event on itself then it will trigger the
    #  'destroy' event on itself passing the additional option dismantle: true.
    #
    #  This implementation may not look exactly like Backbone.Model's
    #  destroy(options), but that's because Backbone's version of the function
    #  is unwinding a lot of asynchronous callback definitions.
    dismantle: (options) ->
        options = _.extend {}, options

        @trigger 'dismantle', @, @collection, options
        options.dismantle = true
        @trigger 'destroy', @, @collection, options
        options.success model, resp, options if options.success?


ORM.parse = (obj, raw, field) ->
    obj[field] = raw[field] if raw[field] isnt undefined

ORM.parse.number = (obj, raw, field, cstor) ->
    return if raw[field] is undefined
    value = cstor raw[field]
    return obj[field] = null if _.isNaN value
    obj[field] = value

ORM.parse.int = (obj, raw, field) ->
    return ORM.parse.number obj, raw, field, (val) -> parseInt val, 10

ORM.parse.float = (obj, raw, field) ->
    return ORM.parse.number obj, raw, field, (val) -> parseFloat val, 10

ORM.parse.enum = (obj, raw, field, Enum) ->
    return if raw[field] is undefined
    obj[field] = Enum[raw[field]]

ORM.parse.datetime = (obj, raw, field) ->
    return if raw[field] is undefined
    return obj[field] = null if raw[field] is null
    obj[field] = new Date raw[field]

ORM.parse.date = (obj, raw, field) ->
    return if raw[field] is undefined
    return obj[field] = null if raw[field] is null
    obj[field] = Datetime.Date raw[field]
