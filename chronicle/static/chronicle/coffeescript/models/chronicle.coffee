# DCMS auto-generated file
# Thu, 7 Nov 2013 07:49:55 -0600 | 6f153b03660b343ba4848e98d7f6af28

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Chronicle.Models'

class Models.Chronicle extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      
        description: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      
      
        description: raw.description
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/chronicle/Chronicle/#{ if @id? then "#{ @id }/" else '' }"

