# DCMS auto-generated file
# 2013-09-17 09:45:58.563058

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
        allowed_ratings: null
        requires_description: null
        type: null
        requires_specification: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            name: raw.name,
            enabled: raw.enabled,
            allowed_ratings: parseInt i for i in raw.allowed_ratings.split ','
            requires_description: raw.requires_description,
            type: Traits.Enums.MeritType.get raw.type
            requires_specification: raw.requires_specification,
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
