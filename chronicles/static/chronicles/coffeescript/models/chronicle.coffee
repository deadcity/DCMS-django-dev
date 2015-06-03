###
  @file  chronicle.coffee
  @brief Models for chronicle objects.
###


Models = Tools.create_namespace 'ORM.Chronicles'


class Models.ChronicleBase extends ORM.BaseModel
    subModelTypeAttribute: '_discriminator'
    subModelTypes:
        'chronicle_template' : 'ChronicleTemplate'
        'chronicle'          : 'Chronicle'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleBase'

    defaults: () ->
        id             : undefined
        _discriminator : undefined

        enabled     : true
        name        : ''
        description : ''

    parse: (raw) ->
        id             : ORM.BaseModel.parse_int_field raw, 'id'
        _discriminator : raw._discriminator

        enabled     : raw.enabled
        name        : raw.name
        description : raw.description

Models.ChronicleBase.setup()


class Models.ChronicleTemplate extends Models.ChronicleBase
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleTemplate'

Models.ChronicleTemplate.setup()


class Models.Chronicle extends Models.ChronicleBase
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/Chronicle'

    # referse relations:
    #   templates -> ORM.Chronicles.ChronicleInheritsTemplate
    #   games -> ORM.Chronicles.Game

Models.Chronicle.setup()


class Models.ChronicleInheritsTemplate extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleInheritsTemplate'

    defaults: () ->
        chronicle_id          : undefined
        chronicle_template_id : undefined

        hide_denied_traits : false

    relations: [
        ORM.relation('chronicle', ORM.Chronicles.Chronicle,
            reverseRelation:
                key: 'templates'
        ),
        ORM.relation('template', ORM.Chronicles.ChronicleTemplate),
    ]

    parse: () ->
        chronicle_id          : ORM.BaseModel.parse_int_field raw, 'chronicle_id'
        chronicle_template_id : ORM.BaseModel.parse_int_field raw, 'chronicle_template_id'

        hide_denied_traits : raw.hide_denied_traits

Models.ChronicleInheritsTemplate.setup()
