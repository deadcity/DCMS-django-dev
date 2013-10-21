# DCMS auto-generated file
# Mon, 21 Oct 2013 07:51:51 -0500 | 2057cbcc2ea7a5396c0bcad396149d55

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.Power extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      
        rating: null
      
        group: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      
      
        rating: parseInt raw.rating, 10
      
      
      
        group: raw.group
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/power/#{ if @id? then "#{ @id }/" else '' }"

