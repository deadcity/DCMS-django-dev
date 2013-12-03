# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:24 -0600 | 8051f770630a4d566d1b7436b1eec506

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'


class Models.MiscTrait extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        requires_description: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        requires_description: raw.requires_description

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/MiscTrait/#{ if @id? then "#{ @id }/" else '' }"

