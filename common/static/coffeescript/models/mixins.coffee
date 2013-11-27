Tools.create_namespace 'Common.Models.Mixins'


Common.Models.Mixins.Validating = class Validating
    @basic_checks:
        non_null  : (v) -> v isnt null and v isnt undefined
        non_empty : (v) -> v isnt ''
        is_number : (v) -> (_.isNumber v) and (not _.isNaN v)
        is_int    : (v) -> Validating.basic_checks.is_number(v) and (v is parseInt v)
        counting  : (v) -> v >  0
        positive  : (v) -> v >= 0

    ###
    Adds 4 new events
        @event 'valid'           (model, attributes, options)
        @event 'invalid'         (model, attributes, options)
        @event 'valid:[field]'   (model, value,      options)
        @event 'invalid:[field]' (model, value,      options)
    ###
    check_valid: (attributes, options) ->
        attr = _.clone attributes ? @attributes
        options = options ? {}
        attr_keys = _.keys attr
        valid = {}
        invalid = _.extend {}, options.html_invalid

        for field, value of attr
            if field of @validation
                if (_.has invalid, field) or not @validation?[field] value
                    invalid[field] = value
                    if not options.silent
                        @trigger "invalid:#{field}", @, value, options
                else
                    valid[field] = value
                    if not options.silent
                        @trigger "valid:#{field}", @, value, options

        if not options.silent
            if _.keys(invalid).length > 0
                @trigger 'invalid', @, invalid, options
            if _.keys(valid).length > 0
                @trigger 'valid', @, valid, options

        return {
            valid: valid
            invalid: invalid
        }


class Common.Models.Mixins.QueryURL
    url: () ->
        base_url = _.result @collection, 'url'
        base_url = base_url.split('?')
        if base_url.length == 1
            return base_url[0] + (if @id? then "#{@id}/" else '')
        else
            return base_url[0] + (if @id? then "#{@id}/?" else '?') + base_url[1]
