# DCMS auto-generated file
# Thu, 14 Nov 2013 16:56:16 -0600 | 16bf6f6d46725c8f5f1fe8c77e150816

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
        chronicle: raw.chronicle
        date: raw.date

    toJSON: () ->
        attr = _.clone @attributes
        attr.chronicle = attr.chronicle.id
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
        attr.chronicle = attr.chronicle.toHumanJSON()
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/chronicle/Game/#{ if @id? then "#{ @id }/" else '' }"

