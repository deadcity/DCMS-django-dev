# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:37 -0600 | 19fd1c41104c00011acf68c6a8f313a3

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'


class Models.Affiliation extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Affiliation/#{ if @id? then "#{ @id }/" else '' }"

