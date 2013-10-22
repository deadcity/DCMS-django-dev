# DCMS auto-generated file
# Mon, 21 Oct 2013 17:12:06 -0500 | adc7be08d3b198e5c65593c5bb07d396

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.Genealogy extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Genealogy/#{ if @id? then "#{ @id }/" else '' }"

