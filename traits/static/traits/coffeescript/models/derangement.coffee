###
  @file  derangement.coffee
  @brief Model for character derangements.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.DerangementType extends Models.TraitType
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/DerangementType"

Models.DerangementType.setup()


class Models.Derangement extends Models.Trait
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Derangement"

    defaults: () ->
        _.extends super,
            derangement_type_id    : undefined
            requires_specification : undefined

    relations: [{
        type: Backbone.HasOne
        key: 'derangement_type'
        relatedModel: Models.DerangementType
        includeInJSON: Models.DerangementType.idAttribute
        autoFetch: true
        keySource: 'derangement_type_id'
    }]

    parse: (raw) ->
        attr = super

        attr.derangement_type_id    = parseInt raw.derangement_type_id, 10
        attr.requires_specification = raw.requires_specification

        attr.derangement_type_id = null if _.isNaN attr.derangement_type_id

        return attr

Models.Derangement.setup()
