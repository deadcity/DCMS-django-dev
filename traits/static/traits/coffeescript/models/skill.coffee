# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:24 -0600 | 50a13ba67df003d372a90ea4f704d93f

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

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else
            attr.type = attr.type.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/Skill/#{ if @id? then "#{ @id }/" else '' }"

