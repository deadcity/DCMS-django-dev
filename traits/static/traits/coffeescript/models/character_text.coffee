# DCMS auto-generated file
# Thu, 14 Nov 2013 16:56:12 -0600 | c588ffd47fd8e6c5201b63372703593e

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

    toJSON: () ->
        attr = _.clone @attributes
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/CharacterText/#{ if @id? then "#{ @id }/" else '' }"

