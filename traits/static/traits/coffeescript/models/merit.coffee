# DCMS auto-generated file
# Mon, 21 Oct 2013 17:12:06 -0500 | 01805419b3e4eec6ca7d99ca628a43b9

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.Merit extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      
        type: null
      
        allowed_ratings: null
      
        requires_specification: null
      
        requires_description: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      
      
        type: Traits.Enums.MeritType.get raw.type
      
      
      
        allowed_ratings: parseInt i, 10 for i in raw.allowed_ratings.split ','
      
      
      
        requires_specification: raw.requires_specification
      
      
      
        requires_description: raw.requires_description
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
        attr.type = attr.type.id
      
      
      
        attr.allowed_ratings = attr.allowed_ratings.join()
      
      
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Merit/#{ if @id? then "#{ @id }/" else '' }"

