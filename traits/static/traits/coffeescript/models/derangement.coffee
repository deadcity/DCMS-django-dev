###
  @file  derangement.coffee
  @brief Model for character derangements.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.DerangementType extends Models.TraitType
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/DerangementType'

Models.DerangementType.setup()


class Models.Derangement extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/traits/Derangement'

    defaults: () ->
        return _.extend super,
            derangement_type_id    : undefined
            requires_specification : undefined

    relations: [
        type: Backbone.HasOne
        key: 'derangement_type'
        relatedModel: Models.DerangementType
        includeInJSON: Models.DerangementType.idAttribute
        autoFetch: true
        keySource: 'derangement_type_id'
    ]

    parse: (raw) ->
        return _.extend super,
            derangement_type_id    : ORM.BaseModel.parse_int_field raw, 'derangement_type_id'
            requires_specification : raw.requires_specification

Models.Derangement.setup()
