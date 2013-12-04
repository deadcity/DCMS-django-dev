# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:39 -0600 | 4f04f4274a03e1902fa5af66d073b1b7

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

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/Power/#{ if @id? then "#{ @id }/" else '' }"

