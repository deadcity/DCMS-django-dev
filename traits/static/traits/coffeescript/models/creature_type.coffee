# DCMS auto-generated file
# Thu, 21 Nov 2013 07:25:38 -0600 | 3dd059481d39f00c145edc2f63ae3ba1

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
        "#{ DCMS.Settings.URL_PREFIX }/api/traits/CreatureType/#{ if @id? then "#{ @id }/" else '' }"

