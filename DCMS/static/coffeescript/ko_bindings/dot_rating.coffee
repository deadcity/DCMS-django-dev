###
    @file  dot_rating.coffee
    @brief Custom Knockout.js binding for a dot rating widget using d3.js.
###


radius = 5
padding = 2

ko.bindingHandlers['dot_rating'] =
    init: (element, value_accessor) ->
        allowed_ratings = value_accessor().allowed_ratings()
        rating_observable = value_accessor().rating
        current_rating = rating_observable()

        $element = $ element
        $element.addClass 'rating-container'

        includes_zero = 0 in allowed_ratings
        max = Math.max.apply null, allowed_ratings

        svg = d3
            .select element
            .append 'svg'
        svg.attr 'height', 10
        svg.attr 'width', 100

        rating_circles = svg
            .append 'g'
            .selectAll 'circle'
            .data _.range 1, max + 1
        rating_circles.enter()
            .append 'circle'
            .classed 'rating-value', true
            .attr 'r', radius
            .attr 'cy', 5
            .attr 'cx', (data) -> data * 2 * (radius + padding)

        # Set initial state.
        rating_circles.classed 'selected', (rating) -> current_rating >= rating

        selectable_circles = rating_circles.filter (rating) -> rating in allowed_ratings
        selectable_circles.classed 'selectable', true

        # Set selecting behavior.
        selectable_circles.on 'mouseover', (pending_rating) ->
            rating_circles.classed 'selecting', (rating) -> pending_rating >= rating
        selectable_circles.on 'mouseout', () ->
            rating_circles.classed 'selecting', false

        # Set selection behavior.
        selectable_circles.on 'click', (new_rating) -> rating_observable new_rating

    update: (element, value_accessor) ->
        current_rating = value_accessor().rating()

        rating_circles = d3
            .select element
            .selectAll 'circle.rating-value'

        rating_circles.classed 'selected', (rating) -> current_rating >= rating
