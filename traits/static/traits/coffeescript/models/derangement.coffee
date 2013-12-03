# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:23 -0600 | 5d3799ddd133169275a90e32b34d0f51

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'


class Models.Derangement extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        type: null
        requires_specification: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        type: Traits.Enums.DerangementType.get raw.type
        requires_specification: raw.requires_specification

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else
            attr.type = attr.type.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Derangement/#{ if @id? then "#{ @id }/" else '' }"

