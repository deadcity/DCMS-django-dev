###
  @file  chronicle.coffee
  @brief Models for chronicle objects.
###


Tools.create_namespace 'ORM.chronicles'


class ORM.chronicles.ChronicleBase extends ORM.BaseModel
    @_polymorphic_on: 'chronicle_type'
    @_polymorphic_identity: {}
    #     'chronicle_template' : 'ChronicleTemplate'
    #     'chronicle'          : 'Chronicle'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleBase'

    defaults: () ->
        id             : undefined
        chronicle_type : undefined

        enabled     : true
        name        : ''
        description : ''

    _parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'
        ORM.parse     parsed, raw, 'chronicle_type'

        ORM.parse parsed, raw, 'enabled'
        ORM.parse parsed, raw, 'name'
        ORM.parse parsed, raw, 'description'

        return parsed

ORM.chronicles.ChronicleBase.reset()


class ORM.chronicles.ChronicleTemplate extends ORM.chronicles.ChronicleBase
    @parent: ORM.chronicles.ChronicleBase

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleTemplate'

ORM.chronicles.ChronicleTemplate.reset()

ORM.polymorphic_identity 'chronicle_template', ORM.chronicles.ChronicleTemplate


class ORM.chronicles.Chronicle extends ORM.chronicles.ChronicleBase
    @parent: ORM.chronicles.ChronicleBase

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/Chronicle'

    # referse relations:
    #   templates -> ORM.Chronicles.ChronicleInheritsTemplate
    #   games -> ORM.Chronicles.Game

ORM.chronicles.Chronicle.reset()

ORM.polymorphic_identity 'chronicle', ORM.chronicles.Chronicle


class ORM.chronicles.ChronicleInheritsTemplate extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleInheritsTemplate'

    defaults: () ->
        chronicle_id          : undefined
        chronicle_template_id : undefined

        hide_denied_traits : false

    _parse: () ->
        parsed = {}

        ORM.parse.int parsed, raw, 'chronicle_id'
        ORM.parse.int parsed, raw, 'chronicle_template_id'

        ORM.parse parsed, raw, 'hide_denied_traits'

        return parsed

ORM.chronicles.ChronicleInheritsTemplate.reset()


ORM.chronicles.Chronicle.has().many 'templates',
    collection: class ChronicleInheritsTemplate_Collection extends Backbone.Collection
        model: ORM.chronicles.ChronicleInheritsTemplate
    inverse: 'chronicle'

ORM.chronicles.ChronicleInheritsTemplate.has().one 'chronicle',
    model: ORM.chronicles.Chronicle
    inverse: 'templates'

ORM.chronicles.ChronicleInheritsTemplate.has().one 'template',
    model: ORM.chronicles.ChronicleTemplate
    inverse: 'chronicles'
