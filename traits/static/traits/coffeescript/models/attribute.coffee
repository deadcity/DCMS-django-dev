###
  @file  attribute.coffee
  @brief Model for character attributes.
###


Models = Tools.create_namespace 'ORM.traits'


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

    relations: [ORM.relation 'attribute_type', ORM.traits.AttributeType]

    parse: (raw) ->
        return _.extend super,
            attribute_type_id : ORM.BaseModel.parse_int_field raw, 'attribute_type_id'

Models.Attribute.setup()
