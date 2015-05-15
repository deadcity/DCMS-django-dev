###
  @file  flaw.coffee
  @brief Model for character flaws.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.FlawType extends Models.TraitType
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/FlawType"

Models.FlawType.setup()


class Models.Flaw extends Models.Flaw
    urlRoot: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Flaw"

    defaults: () ->
        _.extends super,
            flaw_type_id           : undefined
            requires_specification : undefined
            requires_description   : undefined

    relations: [{
        type: Backbone.HasOne
        key: 'flaw_type'
        relatedModel: Models.FlawType
        includeInJSON: Models.FlawType.idAttribute
        autoFetch: true
        keySource: 'flaw_type_id'
    }]

    parse: (raw) ->
        attr = super

        attr.flaw_type_id           = parseInt raw.flaw_type_id, 10
        attr.requires_specification = raw.requires_specification
        attr.requires_description   = raw.requires_description

        attr.flaw_type_id = null if _.isNaN attr.flaw_type_id

        return attr

Models.Flaw.setup()
