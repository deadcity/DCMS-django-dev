# DCMS auto-generated file
# 2013-09-23 10:18:14.789000

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models_NS = Tools.create_namespace 'Traits.Models'

class Models_NS.Skill extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        type: null

    parse: (raw) ->
        {
            id: parseInt raw.id, 10
            enabled: raw.enabled,
            name: raw.name,
            type: Traits.Enums.SkillType.get raw.type
        }

    toJSON: () ->
        attr = _.clone this.attributes

        attr

    toHumanJSON: () ->
        attr = _.clone this.attributes

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Skill/#{ if @id? then "#{@id}/" else '' }"
