SFGTools = Tools.create_namespace 'SVGTools'


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
        el = document.createElementNS('http://www.w3.org/2000/svg', tag_name)
        $el = $(el)
        $el.attr attributes if attributes?
        $el.html content    if content?
        return el
