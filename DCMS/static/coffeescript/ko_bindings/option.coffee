###
    @file  option.coffee
    @brief Custom Knockout.js binding for use with verbose select elements.
###


ko.bindingHandlers['option'] =
    update: (element, value_accessor) ->
        value = ko.utils.unwrapObservable value_accessor()
        ko.selectExtensions.writeValue element, value
