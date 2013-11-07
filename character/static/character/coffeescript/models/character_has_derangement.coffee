# DCMS auto-generated file
# Mon, 4 Nov 2013 08:01:20 -0600 | 26a16b3d31536de2dad4f0371b106f11

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Character.Models'

class Models.CharacterHasDerangement extends Backbone.Model
    defaults:
      
        id: null
      
        character: null
      
        trait: null
      
        specification: null
      
        description: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        character: parseInt raw.character, 10
      
      
      
        trait: raw.trait
      
      
      
        specification: raw.specification
      
      
      
        description: raw.description
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
        attr.character = attr.character.id
      
      
      
        attr.trait = attr.trait.id
      
      
      
      
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
        attr.character = attr.character.toHumanJSON()
      
      
      
        attr.trait = attr.trait.toHumanJSON()
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/character/CharacterHasDerangement/#{ if @id? then "#{ @id }/" else '' }"

