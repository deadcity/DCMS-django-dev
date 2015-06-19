###
  @file  character_has_attribute.coffee
  @brief Model specifying the specific attribute of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasAttribute extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            rating : 1

    _parse: (raw) ->
        return _.extend super,
            rating : ORM.parse.int raw, 'rating'

ORM.characters.CharacterHasAttribute.reset()

ORM.polymorphic_identity 'attribute', ORM.characters.CharacterHasAttribute

ORM.characters.CharacterHasAttribute.has().one 'trait',
    model: ORM.traits.Attribute
    inverse: 'character_has_attribute'

ORM.characters.CharacterHasAttribute.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_attributes'

ORM.characters.Character.has().many 'character_attributes',
    collection: class CharacterHasAttribute_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasAttribute
    inverse: 'character'
