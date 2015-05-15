###
  @file  base_model.coffee
  @brief Base model class for Models in coffeescript.
###


Tools.create_namespace 'ORM'


class ORM.ModelBase extends Backbone.RelationalModel
    constructor: (attributes, options) ->
        id_attribute = @constructor.idAttribute
        if attributes? and id_attribute of attributes
            model = Backbone.Relational.store.find @constructor, attributes[id_attribute]
            if model?
                if options?.parse
                    attrs = (@parse attributes, options) or {}
                else
                    attrs = attributes
                model.set attrs, options
                return model

        return super(attributes, options)

    @idAttribute: 'id'
    @define_property 'idAttribute',
        get: -> @constructor.idAttribute
        set: -> throw new Error 'Cannot set idAttribute on the instance.'
