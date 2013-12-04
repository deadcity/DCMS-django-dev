# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:40 -0600 | 65d886a90ed080238c9604da256d9d42

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Chronicle.Models'


class Models.Game extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        chronicle: null
        date: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        chronicle: Chronicle.Objects.Chronicle.get raw.chronicle
        date: raw.date

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest
            attr.chronicle = attr.chronicle.toJSON options

        else
            attr.chronicle = attr.chronicle.id

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/chronicle/Game/#{ if @id? then "#{ @id }/" else '' }"

