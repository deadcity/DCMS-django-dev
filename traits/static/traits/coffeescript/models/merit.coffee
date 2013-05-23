# DCMS auto-generated file
# 2013-05-23 12:58:28.451149

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models_NS = Tools.create_namespace 'Traits.Models'

class Models_NS.Merit extends Backbone.Model
    defaults:
        id: null
        name: null
        enabled: null
        max_rating: null
        inc_rating: null
        requires_specification: null
        requires_description: null
        type: null
        min_rating: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            name: raw.name,
            enabled: raw.enabled,
            max_rating: parseInt raw.max_rating, 10
            inc_rating: parseInt raw.inc_rating, 10
            requires_specification: raw.requires_specification,
            requires_description: raw.requires_description,
            type: Traits.MeritType.get parseInt raw.type, 10
            min_rating: parseInt raw.min_rating, 10
        }

    toJSON: () ->
        attr = _.clone this.attributes

        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes

        attr

    url: () ->
        "/api/traits/Merit/#{ if @id? then "#{@id}/" else '' }"
