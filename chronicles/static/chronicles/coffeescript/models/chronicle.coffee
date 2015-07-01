###
  @file  chronicle.coffee
  @brief Models for chronicle objects.
###


Tools.create_namespace 'ORM.chronicles'


class ORM.chronicles.ChronicleBase extends ORM.BaseModel
    @polymorphic_on 'chronicle_type'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleBase'

    defaults: () ->
        id             : undefined
        chronicle_type : undefined

        enabled     : true
        name        : ''
        description : ''

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'
        ORM.parse     parsed, raw, 'chronicle_type'

        ORM.parse parsed, raw, 'enabled'
        ORM.parse parsed, raw, 'name'
        ORM.parse parsed, raw, 'description'

        return parsed


class ORM.chronicles.ChronicleTemplate extends ORM.chronicles.ChronicleBase
    @polymorphic_identity 'chronicle_template'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleTemplate'


class ORM.chronicles.Chronicle extends ORM.chronicles.ChronicleBase
    @polymorphic_identity 'chronicle'

    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/Chronicle'

    @has_many 'templates',
        Model     : 'ORM.chronicles.ChronicleInheritsTemplate'
        attribute : 'chronicle_id'

    @has_many 'games',
        Model     : 'ORM.chronicles.Game'
        attribute : 'chronicle_id'


class ORM.chronicles.ChronicleInheritsTemplate extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/chronicles/ChronicleInheritsTemplate'

    defaults: () ->
        chronicle_id          : undefined
        chronicle_template_id : undefined

        hide_denied_traits : false

    parse: () ->
        parsed = {}

        ORM.parse.int parsed, raw, 'chronicle_id'
        ORM.parse.int parsed, raw, 'chronicle_template_id'

        ORM.parse parsed, raw, 'hide_denied_traits'

        return parsed

    @has_one 'chronicle',
        Model : ORM.chronicles.Chronicle

    @has_one 'template',
        Model     : ORM.chronicles.ChronicleTemplate
        attribute : 'chronicle_template_id'
