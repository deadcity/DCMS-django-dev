# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:23 -0600 | d2884db06c579768becf29ff26d3f0d5

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

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/CharacterText/#{ if @id? then "#{ @id }/" else '' }"

