# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:40 -0600 | b96235060595d378ae96bfbcf76d3524

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Chronicle.Models'


class Models.Chronicle extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        description: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        description: raw.description

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/chronicle/Chronicle/#{ if @id? then "#{ @id }/" else '' }"

