# DCMS auto-generated file
# Mon, 21 Oct 2013 07:51:50 -0500 | a7266048154df9984a177971ae5a47ea

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.Flaw extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      
        type: null
      
        requires_specification: null
      
        requires_description: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      
      
        type: Traits.Enums.FlawType.get raw.type
      
      
      
        requires_specification: raw.requires_specification
      
      
      
        requires_description: raw.requires_description
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
        attr.type = attr.type.id
      
      
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/flaw/#{ if @id? then "#{ @id }/" else '' }"

