# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:38 -0600 | 9fbcf6cdebd063d58badc4df09af08e1

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'


class Models.Merit extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        type: null
        allowed_ratings: null
        requires_specification: null
        requires_description: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        type: Traits.Enums.MeritType.get raw.type
        allowed_ratings: parseInt i, 10 for i in raw.allowed_ratings.split ','
        requires_specification: raw.requires_specification
        requires_description: raw.requires_description

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else
            attr.type = attr.type.id
            attr.allowed_ratings = attr.allowed_ratings.join()

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Merit/#{ if @id? then "#{ @id }/" else '' }"

