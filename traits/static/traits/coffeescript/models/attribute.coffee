###
  @file  attribute.coffee
  @brief Model for character attributes.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.AttributeType extends Models.TraitType
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/AttributeType'

Models.AttributeType.setup()


class Models.Attribute extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Attribute'

    defaults: () ->
        return _.extend super,
            attribute_type_id : undefined

    relations: [
        type: Backbone.HasOne
        key: 'attribute_type'
        relatedModel: Models.AttributeType
        includeInJSON: Models.AttributeType.idAttribute
        autoFetch: true
        keySource: 'attribute_type_id'
    ]

    parse: (raw) ->
        return _.extend super,
            attribute_type_id : ORM.BaseModel.parse_int_field raw, 'attribute_type_id'

Models.Attribute.setup()
