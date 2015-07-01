###
  @file  attribute.coffee
  @brief Model for character attributes.
###


Tools.create_namespace 'ORM.traits'


class ORM.traits.AttributeType extends ORM.traits.TraitType


class ORM.traits.Attribute extends ORM.traits.Trait
    @polymorphic_identity 'attribute'

    defaults: () ->
        return _.extend super,
            attribute_type_id : undefined

    parse: (raw) ->
        parsed = super

        ORM.parse.int parsed, raw, 'attribute_type_id'

        return parsed

    @has_one 'attribute_type',
        Model : ORM.traits.AttributeType
