###
  @file  base_model.coffee
  @brief Base model class for Models in coffeescript.
###


Tools.create_namespace 'ORM'


class ORM.ModelBase extends Backbone.RelationalModel
    @idAttribute: 'id'
    @define_property 'idAttribute',
        get: -> @constructor.idAttribute
        set: -> throw new Error 'Cannot set idAttribute on the instance.'
