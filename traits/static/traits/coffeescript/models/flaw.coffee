###
  @file  flaw.coffee
  @brief Model for character flaws.
###


Models = Tools.create_namespace 'ORM.Traits'


class Models.FlawType extends Models.TraitType
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/FlawType'

Models.FlawType.setup()


class Models.Flaw extends Models.Trait
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/traits/Flaw'

    defaults: () ->
        return _.extend super,
            flaw_type_id           : undefined
            requires_specification : undefined
            requires_description   : undefined

    relations: [
        type: Backbone.HasOne
        key: 'flaw_type'
        relatedModel: Models.FlawType
        includeInJSON: Models.FlawType.idAttribute
        autoFetch: true
        keySource: 'flaw_type_id'
    ]

    parse: (raw) ->
        return _.extend super,
            flaw_type_id           : ORM.BaseModel.parse_int_field raw, 'flaw_type_id'
            requires_specification : raw.requires_specification
            requires_description   : raw.requires_description

Models.Flaw.setup()
