###
    @file  available_traits.coffee
    @brief A series of view-model collections for the traits that are available
        for the current character.
###


AvailableTraits = Tools.create_namespace 'VM.trait_access.AvailableTraits'


# Summary traits.
AvailableTraits.creature_type = kb.collectionObservable ORM.traits.CreatureType.store(), VM.traits.Trait, sort_attribute: 'label'
AvailableTraits.genealogy     = kb.collectionObservable ORM.traits.Genealogy.store(),    VM.traits.Trait, sort_attribute: 'label'
AvailableTraits.affiliation   = kb.collectionObservable ORM.traits.Affiliation.store(),  VM.traits.Trait, sort_attribute: 'label'
AvailableTraits.subgroup      = kb.collectionObservable ORM.traits.Subgroup.store(),     VM.traits.Trait, sort_attribute: 'label'

# Detail traits.
AvailableTraits.attribute = kb.collectionObservable ORM.traits.Attribute.store(), VM.traits.Trait
AvailableTraits.skill     = kb.collectionObservable ORM.traits.Skill.store(),     VM.traits.Trait


create = (Model, view_model_collection, attributes, access) ->
    trait = new Model attributes, 'parse': true
    view_model_collection.collection().add trait
    view_model = view_model_collection.viewModelByModel trait
    view_model.access access
    return [trait, view_model]


update_available_summary_traits = (name, character, data) ->
    relation_options = ORM.characters.Character.relations().one[name]
    if _.isString relation_options.Model
        relation_options.Model = Tools.resolve relation_options.Model

    Access = VM.traits.Trait.Access
    Model = relation_options.Model
    collection_observable = AvailableTraits[name]

    for access, models of data
        access = Access[access]

        switch access
            when Access.FORCE
                # TODO (Emery): enforce that this model list only has one item.
                [trait, view_model] = create Model, collection_observable, models[0], access
                @[name] view_model

            when Access.ALLOW
                for attr in models
                    create Model, collection_observable, attr, access

            when Access.DENY
                for attr in models
                    create Model, collection_observable, attr, access
                    # TODO (Emery): (Make design decision.)
                    #   Should this automatically remove these traits from
                    #   the character? (like it does with "HIDE" below)

            when Access.HIDE
                for attr in models
                    trait = Model.store().get attr.id

                    if trait is character[name]
                        if Model is ORM.traits.CreatureType
                            creature_type_mortal = Model.store().findWhere 'name': 'CREATURE_TYPE_MORTAL'
                            character.creature_type = creature_type_mortal
                        else
                            character[name] = null

                    trait?.dismantle()

    return


update_available_traits = (name, Model, character_id, data) ->
    Access = VM.traits.Trait.Access
    collection_observable = AvailableTraits[name]
    CharacterModel = Tools.resolve "ORM.characters.Character#{Model.name}"

    for access, models of data
        access = Access[access]

        switch access
            when Access.FORCE
                for attr in models
                    [trait, view_model] = create Model, collection_observable, attr, access
                    character_trait = CharacterModel.store().findWhere
                        'character_id': character_id
                        'trait_id': trait.id
                    if not character_trait?
                        character_trait = new CharacterModel
                            'character_id': character_id
                            'trait_id': trait.id

            when Access.ALLOW
                for attr in models
                    create Model, collection_observable, attr, access

            when Access.DENY
                for attr in models
                    create Model, collection_observable, attr, access
                    # TODO (Emery): (Make design decision.)
                    #   Should this automatically remove these traits from
                    #   the character? (like it does with "HIDE" below)

            when Access.HIDE
                for trait in models
                    trait = Model.store().get attr.id

                    character_traits = CharacterModel.store().where
                        'character_id': character_id
                        'trait_id': trait.id

                    _.each character_traits, (character_trait) ->
                        character_trait.dismantle()

                    trait.dismantle()

    return


VM.trait_access.update_available_traits = (character, data) ->
    character_id = character.id
    for Model, model_groups of data
        Model = ORM.traits[Model]

        switch Model
            when ORM.traits.CreatureType then update_available_summary_traits 'creature_type', character, model_groups
            when ORM.traits.Genealogy    then update_available_summary_traits 'genealogy',     character, model_groups
            when ORM.traits.Affiliation  then update_available_summary_traits 'affiliation',   character, model_groups
            when ORM.traits.Subgroup     then update_available_summary_traits 'subgroup',      character, model_groups

            when ORM.traits.Attibute then update_available_traits 'attribute', Model, character_id, model_groups
            when ORM.traits.Skill    then update_available_traits 'skill',     Model, character_id, model_groups

    return
