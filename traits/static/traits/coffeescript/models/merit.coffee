# DCMS auto-generated file
# 2013-09-23 10:18:14.789000

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
        enabled: null
        name: null
        type: null
        allowed_ratings: null
        requires_specification: null
        requires_description: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            enabled: raw.enabled,
            name: raw.name,
            type: Traits.Enums.MeritType.get raw.type
            allowed_ratings: parseInt i for i in raw.allowed_ratings.split ','
            requires_specification: raw.requires_specification,
            requires_description: raw.requires_description,
        }

    toJSON: () ->
        attr = _.clone this.attributes
        attr.allowed_ratings = attr.allowed_ratings.join()
        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Merit/#{ if @id? then "#{@id}/" else '' }"
