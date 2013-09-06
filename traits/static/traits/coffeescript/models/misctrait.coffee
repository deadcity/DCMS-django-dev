# DCMS auto-generated file
# 2013-05-23 12:58:28.451149

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models_NS = Tools.create_namespace 'Traits.Models'

class Models_NS.MiscTrait extends Backbone.Model
    defaults:
        id: null
        name: null
        enabled: null
        requires_description: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            name: raw.name,
            enabled: raw.enabled,
            requires_description: raw.requires_description,
        }

    toJSON: () ->
        attr = _.clone this.attributes

        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes

        attr

    url: () ->
        "/api/traits/MiscTrait/#{ if @id? then "#{@id}/" else '' }"
