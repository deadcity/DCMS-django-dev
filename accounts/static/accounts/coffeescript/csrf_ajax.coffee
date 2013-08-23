get_cookie = (name) ->
    if document.cookie? && document.cookie != ''
        cookies = document.cookie.split ';'
        for cookie in cookies
            cookie = $.trim cookie

            if (cookie.substring 0, name.length + 1) == ("#{name}=")
                return decodeURIComponent cookie.substring name.length + 1
    null

is_same_origin = (url) ->
    # URL could be relative, scheme relative, or absolute.
    host = document.location.host  # host + port
    protocol = document.location.protocol
    sr_origin = "//#{host}"
    origin = protocol + sr_origin

    # Allow absolute or scheme relative URLs to same origin.
    return (url is origin or (url.slice 0, origin.length + 1) is ("#{origin}/")) or
        (url is sr_origin or (url.slice 0, sr_origin.length + 1) is ("#{sr_origin}/")) or
        !(/^(\/\/|httpd:|https:).*/.test url)

is_safe_method = (method) ->
    /^(GET|HEAD|OPTIONS|TRACE)$/.test method

$(document).ajaxSend (event, xhr, settings) ->
    if (!is_safe_method settings.type) and (is_same_origin settings.url)
        xhr.setRequestHeader 'X-CSRFToken', get_cookie 'csrftoken'

