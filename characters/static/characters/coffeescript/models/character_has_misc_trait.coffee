###
  @file  character_has_misc_trait.coffee
  @brief Model specifying the specific miscellaneous trait of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasMiscTrait extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            rating      : undefined
            description : undefined

    parse: (raw) ->
        return _.extend super,
            rating      : ORM.parse.int raw, 'rating'
            description : raw.description

ORM.characters.CharacterHasMiscTrait.reset()

ORM.polymorphic_identity 'misc_trait', ORM.characters.CharacterHasMiscTrait

ORM.characters.CharacterHasMiscTrait.has().one 'trait',
    model: ORM.traits.MiscTrait
    inverse: 'character_has_misc_trait'

ORM.characters.CharacterHasMiscTrait.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_misc_traits'

ORM.characters.Character.has().many 'character_misc_traits',
    collection: class CharacterHasMiscTrait_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasMiscTrait
    inverse: 'character'
