# DCMS auto-generated file
# Thu, 14 Nov 2013 16:56:13 -0600 | a4cdf0a183ef65ef410b4423f8050b8f

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


Models = Tools.create_namespace 'Traits.Models'


class Models.CreatureType extends Backbone.Model
    defaults:
        id: null
        enabled: null
        name: null
        genealogy_name: null
        affiliation_name: null
        subgroup_name: null
        power_name: null

    parse: (raw) ->
        id: parseInt raw.id, 10
        enabled: raw.enabled
        name: raw.name
        genealogy_name: raw.genealogy_name
        affiliation_name: raw.affiliation_name
        subgroup_name: raw.subgroup_name
        power_name: raw.power_name

    toJSON: () ->
        attr = _.clone @attributes
        attr

    toHumanJSON: () ->
        attr = _.clone @attributes
        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/CreatureType/#{ if @id? then "#{ @id }/" else '' }"

