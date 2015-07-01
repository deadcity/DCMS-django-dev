###
  @file  user.coffee
  @brief Model representing a user.
###


Tools.create_namespace 'ORM.auth'


class ORM.auth.User extends ORM.BaseModel
    urlRoot: () ->
        DCMS.Settings.URL_PREFIX + '/rest/accounts/User'

    defaults: () ->
        id : undefined

        username   : undefined
        first_name : undefined
        last_name  : undefined
        email      : undefined

        # password

        is_staff     : false
        is_active    : true
        is_superuser : false

        last_login  : undefined
        date_joined : undefined

    parse: (raw) ->
        parsed = {}

        ORM.parse.int parsed, raw, 'id'

        ORM.parse parsed, raw, 'username'
        ORM.parse parsed, raw, 'first_name'
        ORM.parse parsed, raw, 'last_name'
        ORM.parse parsed, raw, 'email'

        # password

        ORM.parse parsed, raw, 'is_staff'
        ORM.parse parsed, raw, 'is_active'
        ORM.parse parsed, raw, 'is_superuser'

        ORM.parse.datetime parsed, raw, 'last_login'
        ORM.parse.datetime parsed, raw, 'date_joined'

        return parsed
