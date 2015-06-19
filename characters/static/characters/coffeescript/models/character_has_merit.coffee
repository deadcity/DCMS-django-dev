###
  @file  character_has_merit.coffee
  @brief Model specifying the specific merit of a specific character.
###


Tools.create_namespace 'ORM.characters'


class ORM.characters.CharacterHasMerit extends ORM.characters.CharacterHasTrait
    @parent: ORM.characters.CharacterHasTrait

    defaults: () ->
        return _.extend super,
            rating        : undefined
            specification : undefined
            description   : undefined

    _parse: (raw) ->
        return _.extend super,
            rating        : ORM.parse.int raw, 'rating'
            specification : raw.specification
            description   : raw.description

ORM.characters.CharacterHasMerit.reset()

ORM.polymorphic_identity 'merit', ORM.characters.CharacterHasMerit

ORM.characters.CharacterHasMerit.has().one 'trait',
    model: ORM.traits.Merit
    inverse: 'character_has_merit'

ORM.characters.CharacterHasMerit.has().one 'character',
    model: ORM.characters.Character
    inverse: 'character_merits'

ORM.characters.Character.has().many 'character_merits',
    collection: class CharacterHasMerit_Collection extends Backbone.Collection
        model: ORM.characters.CharacterHasMerit
    inverse: 'character'
