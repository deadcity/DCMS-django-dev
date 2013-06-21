Datetime = Tools.create_namespace 'Datetime'

Datetime.MAX_DATE = 100000 * 24 * 60 * 60 * 1000000;

_truncate = (x) -> parseInt x, 10


###
  Simple example: Find the tens and hundredths of x = 234.117.
    call:    _non_standard_base 234.117, 10, 100
    returns: [23, 4, 11.7]

  Practical example: Extract the days, hours and minutes from 30.2 hours.
    call:    _non_standard_base 30.2, 24, 60
    returns: [1, 6, 12]

  @brief Break out the overflow and underflow from a number with a non-standard base.
  @arg x The number to break apart.
  @arg upper The upper limit of x.  (Quantity of x per upper unit.)
  @arg lower Quantity of lower unit per unit of x.
###
_non_standard_base = (x, upper, lower) ->
    over  = _truncate x / upper
    under = x - _truncate x
    mid   = _truncate x % upper

    [
        if over  != 0 then over          else null
        mid
        if under != 0 then under * lower else null
    ]


Datetime.Month = new Enum.Enum [
    { name: 'January',   value:  1 }
    { name: 'February',  }
    { name: 'March',     }
    { name: 'April',     }
    { name: 'May',       }
    { name: 'June',      }
    { name: 'July',      }
    { name: 'August',    }
    { name: 'September', }
    { name: 'October',   }
    { name: 'November',  }
    { name: 'December',  }
]

Datetime.Day_of_Week = new Enum.Enum [
    { name: 'Sunday',    value: 1 }
    { name: 'Monday',    }
    { name: 'Tuesday',   }
    { name: 'Wednesday', }
    { name: 'Thursday',  }
    { name: 'Friday',    }
    { name: 'Saturday',  }
]


class Datetime.Date
    constructor: (value, options) ->
        options = options ? {}

        if _.isNumber value
            date = new window.Date value
        else if _.isString value
            date = new window.Date value
        else if value instanceof window.Date
            date = value

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
                @_month = value
            else
                @_from_date(@to_builtin_date().setDate value)
        @_day

    # Milliseconds since epoch.
    time: () ->
        @to_builtin_date().getTime()

    toString: () ->
        "#{@_year}-#{@_month.value}-#{@_day}"

    valueOf: () ->
        @time()

    @today: () ->
        new Datetime.Date new Date()


class Datetime.Time
    constructor: (value, options) ->
        options = options ? {}

        if _.isNumber value
            time = new Date value

        # TODO(emery): parse manually
        else if _.isString value
            time = new Date value

        else if value instanceof Date
            time = value

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
            [day, @_hour, minute] = _non_standard_base value, 24, 60
            @minute minute
        @_hour

    minute: (value) ->
        if value?
            [hour, @_minute, second] = _non_standard_base value, 60, 60
            @hour hour
            @second second
        @_minute

    second: (value) ->
        if value?
            [minute, @_second, millisecond] = _non_standard_base value, 60, 1000
            @minute minute
            @millisecond millisecond
        @_second

    millisecond: (value) ->
        if value?
            [second, @_millisecond, microsecond] = _non_standard_base value, 1000, 1000
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

    valueOf: () ->
        @time()
