# DCMS auto-generated file
# Mon, 21 Oct 2013 07:51:51 -0500 | ecd5f1b9e68f6aa014a34c214763c003

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'

class Models.Skill extends Backbone.Model
    defaults:
      
        id: null
      
        enabled: null
      
        name: null
      
        type: null
      

    parse: (raw) ->
      
      
        id: parseInt raw.id, 10
      
      
      
        enabled: raw.enabled
      
      
      
        name: raw.name
      
      
      
        type: Traits.Enums.SkillType.get raw.type
      
      

    toJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
        attr.type = attr.type.id
      
      
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
      
      
      
      
      
      
      
      
      
      
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/skill/#{ if @id? then "#{ @id }/" else '' }"

