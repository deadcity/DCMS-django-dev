# DCMS auto-generated file
# Wed, 23 Oct 2013 07:49:01 -0500 | 438d46f42269fa15a2d4dbdbb56f7e28

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.CharacterText extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      
        hide_from_player: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      
      
        hide_from_player: raw.hide_from_player
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/CharacterText/#{ if @id? then "#{ @id }/" else '' }"

