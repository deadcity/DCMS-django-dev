# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:23 -0600 | 548a57198b0a41a8aff62b7ee8bdfaa4

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

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/CombatTrait/#{ if @id? then "#{ @id }/" else '' }"
