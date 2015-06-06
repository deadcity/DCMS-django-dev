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
        raw = super

        return {
            id : ORM.parse.int raw, 'id'

            username   : raw.username
            first_name : raw.first_name
            last_name  : raw.last_name
            email      : raw.email

            # password

            is_staff     : raw.is_staff
            is_active    : raw.is_active
            is_superuser : raw.is_superuser

            last_login  : ORM.parse.datetime raw, 'last_login'
            date_joined : ORM.parse.datetime raw, 'date_joined'
        }

ORM.auth.User.reset()
