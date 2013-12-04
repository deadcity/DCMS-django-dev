# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:37 -0600 | b88cfb149427f73a46123dbd9e128007

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'


class Models.Attribute extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        type: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        type: Traits.Enums.AttributeType.get raw.type

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else
            attr.type = attr.type.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Attribute/#{ if @id? then "#{ @id }/" else '' }"

