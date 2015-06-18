Datetime = Tools.create_namespace 'Datetime'

Datetime.MILLISECONDS_PER_DAY = 24 * 60 * 60 * 1000
Datetime.MAX_DATE = 100000000 * Datetime.MILLISECONDS_PER_DAY;

_truncate = (x) -> parseInt x, 10


###
  Simple example: Find the tens and hundredths of x = 234.117.
    call:    _non_standard_base 10, 234.117, 100
    returns: [23, 4, 11.7]

  Practical example: Extract the days, hours and minutes from 30.2 hours.
    call:    _non_standard_base 24, 30.2, 60
    returns: [1, 6, 12]

  @brief Break out the overflow and underflow from a number with a non-standard base.
  @arg upper The upper limit of x.  (Quantity of x per upper unit.)
  @arg x The number to break apart.
  @arg lower Quantity of lower unit per unit of x.
###
_non_standard_base = (upper, x, lower) ->
    over  = _truncate x / upper
    mid   = _truncate x % upper
    under = x - _truncate x

    [
        if over  != 0 then over          else null
        mid
        if under != 0 then under * lower else null
    ]


Datetime.Month = Tools.enum 'Month', [
    'January'
    'February'
    'March'
    'April'
    'May'
    'June'
    'July'
    'August'
    'September'
    'October'
    'November'
    'December'
]

Datetime.Day_of_Week = Tools.enum 'Day_of_Week', [
    'Sunday'
    'Monday'
    'Tuesday'
    'Wednesday'
    'Thursday'
    'Friday'
    'Saturday'
]


class Datetime.Date
    constructor: (value, options) ->
        options = options ? {}

        if value instanceof Datetime.Date
            @_year  = value._year
            @_month = value._month
            @_day   = value._day
            return @

        date = switch
            when value instanceof window.Date then value
            when _.isNumber value             then new window.Date value
            when _.isString value
                options.UTC = true
                new window.Date value
            else null

        if date?
            if options.UTC then @_from_utc_date date else @_from_date date

    _from_date: (date) ->
        @_year  = date.getFullYear()
        @_month = Datetime.Month.get date.getMonth() + 1
        @_day   = date.getDate()
        @

    _from_utc_date: (date) ->
        @_year  = date.getUTCFullYear()
        @_month = Datetime.Month.get date.getUTCMonth() + 1
        @_day   = date.getUTCDate()
        @

    to_builtin_date: () ->
        new window.Date @_year, @_month - 1, @_day

    year: (value) ->
        if value? then @_year = value
        @_year

    month: (value) ->
        if value?
            target = Datetime.Month.get value
            if target?
                @_month = target
            else
                @_from_date(@to_builtin_date().setMonth value - 1)
        @_month

    day: (value) ->
        if value?
            if target <= 28
                @_day = value
            else
                @_from_date(@to_builtin_date().setDate value)
        @_day

    # Milliseconds since epoch.
    time: () ->
        @to_builtin_date().getTime()

    day_of_week: () ->
        Datetime.Day_of_Week @to_builtin_date().getDay() + 1

    toString: () ->
        "#{ @_year }-#{ if @_month < 10 then '0' else '' }#{ @_month.value }-#{ if @_day < 10 then '0' else '' }#{ @_day }"

    valueOf: () ->
        @time()

    @today: () ->
        new Datetime.Date new Date()


class Datetime.Time
    constructor: (value, options) ->
        options = options ? {}

        if value instanceof Datetime.Time
            @_hour        = value._hour
            @_minute      = value._minute
            @_second      = value._second
            @_millisecond = value._millisecond
            return @

        time = switch
            when value instanceof Date then value
            when _.isNumber value      then new Date value
            when _.isString value      then new Date value
            else null

        if time?
            if options.UTC then @_from_utc_time time else @_from_time time

    _from_time: (time) ->
        @_hour        = time.getHours()
        @_minute      = time.getMinutes()
        @_second      = time.getSeconds()
        @_millisecond = time.getMilliseconds()
        @

    _from_utc_time: (time) ->
        @_hour        = time.getUTCHours()
        @_minute      = time.getUTCMinutes()
        @_second      = time.getUTCSeconds()
        @_millisecond = time.getUTCMilliseconds()
        @

    hour: (value) ->
        if value?
            [day, @_hour, minute] = _non_standard_base 24, value, 60
            @minute minute
        @_hour

    minute: (value) ->
        if value?
            [hour, @_minute, second] = _non_standard_base 60, value, 60
            @hour hour
            @second second
        @_minute

    second: (value) ->
        if value?
            [minute, @_second, millisecond] = _non_standard_base 60, value, 1000
            @minute minute
            @millisecond millisecond
        @_second

    millisecond: (value) ->
        if value?
            [second, @_millisecond, microsecond] = _non_standard_base 1000, value, 1000
            @second second
        @_millisecond

    # Milliseconds since 00:00:00.
    time: () ->
        new Date(0).setHours(
            @_hour,
            @_minute,
            @_second,
            @_millisecond
        ).valueOf()

    toString: () ->
        "#{ @_hour }:#{ if @_minute < 10 then '0' else '' }#{ @_minute }:#{ if @_second < 10 then '0' else '' }#{ @_second }"

    valueOf: () ->
        @time()
