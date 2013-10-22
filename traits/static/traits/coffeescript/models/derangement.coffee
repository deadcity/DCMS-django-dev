# DCMS auto-generated file
# Mon, 21 Oct 2013 17:12:06 -0500 | d4ba2832bd91643afec632b991d9f8ba

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.Derangement extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      
        type: null
      
        requires_specification: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      
      
        type: Traits.Enums.DerangementType.get raw.type
      
      
      
        requires_specification: raw.requires_specification
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
        attr.type = attr.type.id
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Derangement/#{ if @id? then "#{ @id }/" else '' }"

