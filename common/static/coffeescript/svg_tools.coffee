SVGTools = Tools.create_namespace 'SVGTools'


SVGTools.svg_namespace_uri = 'http://www.w3.org/2000/svg'


SVGTools.is_svg_element = (node) ->
    node.nodeType is 1 and node.namespaceURI is SVGTools.svg_namespace_uri


###
  A base class to use for Backbone-Views who's root elements are in the
  SVG namespace.
###

class SVGTools.SVGView extends Backbone.View
    _ensureElement: () ->
        if not @el?
            attrs = _.clone _.result @, 'attributes'
            if @id?
                attrs.id = _.result @, 'id'
            if @className?
                attrs['class'] = _.result @, 'className'
            $el = @make _.result(@, 'tagName'), attrs
            @setElement $el, false
        else
            @setElement _.result(@, 'el'), false

    make: (tag_name, attributes, content) ->
        el = document.createElementNS SVGTools.svg_namespace_uri, tag_name
        $el = $(el)
        $el.attr attributes if attributes?
        $el.html content    if content?
        return el


###
  Add support for adding class manipulation of SVG nodes through jQuery.
###


get_class_name = (node) ->
    if SVGTools.is_svg_element node then node.className.baseVal else node.className


add_class_gen = (orig_add_class) ->
    return (value) ->
        if _.isFunction value
            return @each (j) ->
                jQuery(@).addClass value.call @, j, get_class_name @

        if typeof value isnt 'string' or not value
            return

        class_names = value ? ''
        new_classes = class_names.match /\S+/g

        @each () ->
            if SVGTools.is_svg_element @
                node = @
                old_classes = node.className.baseVal.match /\S+/g
                old_classes = old_classes ? []
                for cl in new_classes
                    if not (cl in old_classes)
                        old_classes.push cl
                node.className.baseVal = old_classes.join ' '
            else
                orig_add_class.apply $(@), [class_names]
$.fn.addClass = add_class_gen $.fn.addClass


remove_class_gen = (orig_remove_class) ->
    return (value) ->
        if _.isFunction value
            return @each (j) ->
                jQuery(@).removeClass value.call @, j, get_class_name @

        if typeof value isnt 'string' or not value
            return

        class_names = value ? ''
        removing_classes = class_names.match /\S+/g

        @each () ->
            if SVGTools.is_svg_element @
                node = @
                old_classes = node.className.baseVal.match /\S+/g
                old_classes = old_classes ? []
                old_classes = _.without old_classes, removing_classes...
                node.className.baseVal = old_classes.join ' '
            else
                orig_remove_class.apply $(@), [class_names]
$.fn.removeClass = remove_class_gen $.fn.removeClass


# toggle_class_gen = (orig_toggle_class) ->
#     return (value, state) ->
#         if _.isFunction value
#             return @each (j) ->
#                 jQuery(@).toggleClass value.call(@, j, get_class_name(@), state), state

#         @each () ->
#             if SVGTools.is_svg_element @
#                 pass
#             else
#                 orig_toggle_class.apply $(@), [class_names]


has_class_gen = (orig_has_class) ->
    return (selector) ->
        target = " #{selector} "
        i = 0
        l = @length

        _.some @, (node) ->
            class_name = get_class_name node
            " #{class_name} ".replace(/[\t\r\n\f]/g, " ").indexOf(target) >= 0
