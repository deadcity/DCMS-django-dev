# DCMS auto-generated file
# Wed, 23 Oct 2013 07:49:01 -0500 | e32a4739c06ce212561171e7f5612944

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.CombatTrait extends Backbone.Model
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
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/CombatTrait/#{ if @id? then "#{ @id }/" else '' }"

