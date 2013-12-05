# DCMS auto-generated file
# Sat, 30 Nov 2013 05:25:23 -0600 | 742cad7f1465dc93b286523d9bfb77d4

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

    toJSON: (options) ->
        options = {} if not options?
        attr = _.clone @attributes

        if options.nest

        else

        attr

    url: () ->
        "#{ DCMS.Settings.URL_PREFIX }/traits/CreatureType/#{ if @id? then "#{ @id }/" else '' }"

