# DCMS auto-generated file
# Mon, 21 Oct 2013 07:51:49 -0500 | cc8df83d18548e3f8f239755a5efe4c0

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
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
        attr.type = attr.type.id
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/attribute/#{ if @id? then "#{ @id }/" else '' }"

