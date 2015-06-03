###
  @file  base_model.coffee
  @brief Base model class for Models in coffeescript.
###


Tools.create_namespace 'ORM'

Backbone.Relational.store.addModelScope ORM

ORM.relation = (key, RelatedModel, options = {}) ->
    return _.defaults {}, options,
        type          : Backbone.HasOne
        key           : key
        relatedModel  : RelatedModel
        includeInJSON : RelatedModel.idAttribute
        autoFetch     : true
        keySource     : key + '_id'

ORM.relation_collection = (key, RelatedModel, options = {}) ->
    return _.defaults {}, options,
        type          : Backbone.HasMany
        key           : key
        relatedModel  : RelatedModel
        includeInJSON : false


class ORM.BaseModel extends Backbone.RelationalModel
    @idAttribute: 'id'
    @define_property 'idAttribute',
        get: -> @constructor.idAttribute
        set: -> throw new Error 'Cannot set idAttribute on the instance.'

    @parse_num_field: (raw, field, cstor) ->
        return undefined if raw[field] is undefined
        value = cstor raw[field]
        return null if _.isNaN value
        return value

    @parse_int_field: (raw, field) ->
        return BaseModel.parse_num_field raw, field, (val) -> parseInt val, 10

    @parse_float_field: (raw, field) ->
        return BaseModel.parse_num_field raw, field, (val) -> parseFloat val, 10

    @parse_datetime_field: (raw, field) ->
        return undefined if raw[field] is undefined
        return null if raw[field] is null
        return new Date raw[field]

    @parse_date_field: (raw, field) ->
        return undefined if raw[field] is undefined
        return null if raw[field] is null
        return new Datetime.Date raw[field]
