###
    @file  accounts/coffeescript/viewmodels/user.coffee
    @brief Standard view-model for User.
###


Tools.create_namespace 'VM.auth'


class VM.auth.User extends VM.BaseViewModel
    constructor: (model, options) ->
        super

        @name = ko.computed =>
            name = ((@first_name() ? '') + ' ' + (@last_name() ? '')).trim()
            return name if name != ''
            name = @username()
            return name.trim() if name?
            return ''
