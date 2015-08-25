###
    @file  trait.coffee
    @brief View-models and related objects for traits.
###


Tools.create_namespace 'VM.traits'


class VM.traits.Trait extends VM.BaseViewModel
    @Access: Tools.enum 'Access', [
        'FORCE'
        'ALLOW'
        'DENY'
        'HIDE'
    ]

    constructor: (model, options) ->
        super

        @access = ko.observable this.constructor.Access._UNDEF

    copy: (other_vm) ->
        super
        @access other_vm?.access()
        return @
