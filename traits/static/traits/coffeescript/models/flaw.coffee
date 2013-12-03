# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:24 -0600 | bc8ee83bb51ca93ebe8bc8f5842d3be3

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'


class Models.Flaw extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        type: null
        requires_specification: null
        requires_description: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        type: Traits.Enums.FlawType.get raw.type
        requires_specification: raw.requires_specification
        requires_description: raw.requires_description

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else
            attr.type = attr.type.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Flaw/#{ if @id? then "#{ @id }/" else '' }"

