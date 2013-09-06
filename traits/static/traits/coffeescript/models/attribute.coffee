# DCMS auto-generated file
# 2013-08-24 15:52:40.539000

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models_NS = Tools.create_namespace 'Traits.Models'

class Models_NS.Attribute extends Backbone.Model
    defaults:
        id: null
        name: null
        enabled: null
        type: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            name: raw.name,
            enabled: raw.enabled,
            type: Traits.Enums.AttributeType.get parseInt raw.type, 10
        }

    toJSON: () ->
        attr = _.clone this.attributes

        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes

        attr

    url: () ->
        "/api/traits/Attribute/#{ if @id? then "#{@id}/" else '' }"
