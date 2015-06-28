###
  @file  base_model.coffee
  @brief Base model class for Models in coffeescript.
###


Tools.create_namespace 'ORM'


ORM.polymorphic_identity = (value, Model) ->
    # Due to the way coffeescript handles inheriting static members, this
    # should be the same object as the base model's `_polymorphic_identity`.
    Model._polymorphic_identity[value] = Model


class ORM.BaseModel extends Supermodel.Model
    constructor: (attrs, options) ->
        if options?._force_new
            super

            polymorphic_on = @constructor._polymorphic_on
            if polymorphic_on? and not attrs[polymorphic_on]?
                @once 'change:' + polymorphic_on, @_update_polymorphic_identity, @

            # When a model is destoryed, remove all references so it can be
            # cleaned up.  This will not prevent already queued events from
            # firing.
            @on 'destroy', =>
                @stopListening()
                @off()

            return @

        options = _.extend {}, options, _force_new: true
        return @constructor.create attrs, options

    _update_polymorphic_identity: (model, value, options) ->
        target_model = model.constructor._polymorphic_identity[value]
        model.__proto__ = target_model.prototype
        model.initialize model.attributes, options
        model.fetch()

    ## Destroy this object on the client only. (No effect on the server.)
    #
    #  This is basically the exact same implementation as Backbone.Model's
    #  destroy(options) except that it doesn't sync with the server.  It will
    #  trigger the 'dismantle' event on itself then it will trigger the
    #  'destroy' event on itself passing the additional option dismantle: true.
    #
    #  This implementation may not look exactly like Backbone.Model's
    #  destroy(options), but that's because it is unwinding a lot of
    #  asynchronous callback definitions.
    dismantle: (options) ->
        options = _.extend {}, options

        @trigger 'dismantle', @, @collection, options
        options.dismantle = true
        @trigger 'destroy', @, @collection, options
        options.success model, resp, options if options.success?

    ## Override this to provide parsing functionality [instead of `parse`].
    _parse: (raw) -> raw

    ## Do not override this for normal parsing functionality.
    #
    #  Supermodel.js goes against standard Backbone.js and expects `parse` to
    #  modify it's dictionary of attributes instead of handling whatever is
    #  returned.  This function will take care of that, copying over any parsed
    #  attributes and clearing out any that were not parsed.
    parse: (raw) ->
        raw_ = _.clone @_parse raw

        # Clear out old values of `raw`.
        for key of raw
            delete raw[key]

        super _.extendOwn raw, raw_


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
