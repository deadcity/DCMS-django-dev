###
  @file  attribute.coffee
  @brief Model for character attributes.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.AttributeType extends Models.TraitType
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/AttributeType"

Models.AttributeType.setup()


class Models.Attribute extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Attribute"

    defaults: () ->
        _.extends super,
            attribute_type_id : undefined

    relations: [{
        type: Backbone.HasOne
        key: 'attribute_type'
        relatedModel: Models.AttributeType
        includeInJSON: Models.AttributeType.idAttribute
        autoFetch: true
        keySource: 'attribute_type_id'
    }]

    parse: (raw) ->
        attr = super

        attr.attribute_type_id = parseInt raw.attribute_type_id, 10

        attr.attribute_type_id = null if _.isNaN attr.attribute_type_id

        return attr

Models.Attribute.setup()
