# DCMS auto-generated file
# Thu, 14 Nov 2013 16:56:12 -0600 | 4cae998f06750f945e4827da2355192c

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

    toJSON: () ->
        attr = _.clone @attributes
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Affiliation/#{ if @id? then "#{ @id }/" else '' }"

