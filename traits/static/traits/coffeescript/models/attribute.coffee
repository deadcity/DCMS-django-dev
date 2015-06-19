###
  @file  attribute.coffee
  @brief Model for character attributes.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.AttributeType extends ORM.traits.TraitType

ORM.traits.AttributeType.reset()


class ORM.traits.Attribute extends ORM.traits.Trait
    @parent: ORM.traits.Trait

    defaults: () ->
        return _.extend super,
            attribute_type_id : undefined

    _parse: (raw) ->
        return _.extend super,
            attribute_type_id : ORM.parse.int raw, 'attribute_type_id'

ORM.traits.Attribute.reset()

ORM.polymorphic_identity 'attribute', ORM.traits.Attribute

ORM.traits.Attribute.has().one 'attribute_type',
    model: ORM.traits.AttributeType
    inverse: 'attributes'
