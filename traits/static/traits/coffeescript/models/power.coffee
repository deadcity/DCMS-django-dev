# DCMS auto-generated file
# Mon, 21 Oct 2013 17:12:07 -0500 | 21caa9ce39c9696bb57f201de369f596

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
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Power/#{ if @id? then "#{ @id }/" else '' }"

