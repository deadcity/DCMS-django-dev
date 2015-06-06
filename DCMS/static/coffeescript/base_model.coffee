###
  @file  base_model.coffee
  @brief Base model class for Models in coffeescript.
###


Tools.create_namespace 'ORM.parse'


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
            return @

        options = _.extend {}, options, _force_new: true
        return @constructor.create attrs, options

    _update_polymorphic_identity: (model, value, options) ->
        target_model = model.constructor._polymorphic_identity[value]
        model.__proto__ = target_model.prototype
        model.initialize model.attributes, options
        model.fetch()


ORM.parse.number = (raw, field, cstor) ->
    return undefined if raw[field] is undefined
    value = cstor raw[field]
    return null if _.isNaN value
    return value

ORM.parse.int = (raw, field) ->
    return ORM.parse.number raw, field, (val) -> parseInt val, 10

ORM.parse.float = (raw, field) ->
    return ORM.parse.number raw, field, (val) -> parseFloat val, 10

ORM.parse.datetime = (raw, field) ->
    return undefined if raw[field] is undefined
    return null if raw[field] is null
    return new Date raw[field]

ORM.parse.date = (raw, field) ->
    return undefined if raw[field] is undefined
    return null if raw[field] is null
    return new Datetime.Date raw[field]
