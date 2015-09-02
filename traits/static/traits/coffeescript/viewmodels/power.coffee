###
    @file  power.coffee
    @brief View-models and related objects for powers.
###


Tools.create_namespace 'VM.traits'


class VM.traits.PowerGroup extends VM.traits.Trait
    constructor: (model, options) ->
        super

        @configure_has_many 'powers', VM.traits.Power, sort_attribute: 'rating'


class VM.traits.Power extends VM.traits.Trait
    constructor: (model, options) ->
        super

        @label_with_rating = ko.computed =>
            "#{@rating()} - #{@label()}"
