# DCMS auto-generated file
# Thu, 14 Nov 2013 16:56:14 -0600 | 76a70b80b00a7fbcfeb974d5b21d12ef

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

    toJSON: () ->
        attr = _.clone @attributes
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/MiscTrait/#{ if @id? then "#{ @id }/" else '' }"

