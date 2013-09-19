
(function () {

var Datetime = Tools.create_namespace('Datetime');

Datetime.MAX_DATE = 100000 * 24 * 60 * 60 * 1000000;

Datetime.Month = new Enum.Enum([
    { name: 'January',   value:  1 },
    { name: 'February',  },
    { name: 'March',     },
    { name: 'April',     },
    { name: 'May',       },
    { name: 'June',      },
    { name: 'July',      },
    { name: 'August',    },
    { name: 'September', },
    { name: 'October',   },
    { name: 'November',  },
    { name: 'December',  },
]);

Datetime.Day_of_Week = new Enum.Enum([
    { name: 'Sunday',    value: 1 },
    { name: 'Monday',    },
    { name: 'Tuesday',   },
    { name: 'Wednesday', },
    { name: 'Thursday',  },
    { name: 'Friday',    },
    { name: 'Saturday',  },
]);


var parse_int = function (field) {
    return function (obj, value) {
        obj.set(field, parseInt(value));
    }
};

var parse_month = function (date, value) {
    if (_.isNumber(value)) {
        date.set('month', Datetime.Month.get(value));
    } else if (_.isString(value)) {
        var num = parseInt(value);
        if (_.isNaN(num)) {
            date.set('month', Datetime.Month[value]);
        } else {
            date.set('month', Datetime.Month.get(num));
        }
    }
};


Datetime.Date = Backbone.Model.extend({
    defaults: {
        year:  1970,
        month: Datetime.Month.January,
        day:   1,
    },

    constructor: function (data, options) {
        var opts = options || {};

        // Parse from number.
        if (_.isNumber(data)) {
            var date = new Date(data);
            data = opts.UTC ? {
                year:  date.getUTCFullYear(),
                month: date.getUTCMonth() + 1,
                day:   date.getUTCDate(),
            } : {
                year:  date.getFullYear(),
                month: date.getMonth() + 1,
                day:   date.getDate(),
            };
        }

        // Parse from string.
        else if (_.isString(data)) {
            var date = new Date(data);
            // TODO(emery): Parse date manually.
            //              This date will be wrong if someone types:
            //              '2013-01-16 18:00'.
            data = date.getTime() % (24*60*60*1000) == 0 ? {
                year:  date.getUTCFullYear(),
                month: date.getUTCMonth() + 1,
                day:   date.getUTCDate(),
            } : {
                year:  date.getFullYear(),
                month: date.getMonth() + 1,
                day:   date.getDate(),
            };
        }

        // Parse from builtin Date().
        else if (data instanceof Date) {
            data = opts.UTC ? {
                year:  data.getUTCFullYear(),
                month: data.getUTCMonth() + 1,
                day:   data.getUTCDate(),
            } : {
                year:  data.getFullYear(),
                month: data.getMonth() + 1,
                day:   data.getDate(),
            };
        }

        // Call parent constructor.
        this.__proto__.__proto__.constructor.apply(this, arguments);
    },

    initialize: function (attributes, options) {
        this.on('change:year',  parse_int('year'));
        this.on('change:month', parse_month);
        this.on('change:day',   parse_int('day'));

        if (attributes) {
            if (attributes.year  !== undefined) parse_int('year')(this, attributes.year);
            if (attributes.month !== undefined) parse_month(this, attributes.month);
            if (attributes.day   !== undefined) parse_int('day')(this, attributes.day);
        }
    },

    to_builtin_Date: function () {
        return new Date(this.attributes.year,
                        this.attributes.month - 1,
                        this.attributes.day);
    },

    day: function (value) {
        if (value !== undefined) this.set('day', value);
        return this.get('day');
    },

    day_of_week: function () {
        return Datetime.Day_of_Week.get(this.to_builtin_Date().getDay() + 1);
    },

    month: function (value) {
        if (value !== undefined) this.set('month', value);
        return this.get('month');
    },

    year: function (value) {
        if (value !== undefined) this.set('year', value);
        return this.get('year');
    },

    // Milliseconds since epoch.
    time: function () {
        return this.to_builtin_Date().getTime();
    },

    to_string: function (format) {
        format = format || '%YEAR%-%MONTH%-%DAY%';
        var day_of_week = this.day_of_week();
        return String.template_replace(format, {
            YEAR  : String.left_pad(this.attributes.year,                   '0', 4),
            MONTH : String.left_pad(this.attributes.month.attributes.value, '0', 2),
            DAY   : String.left_pad(this.attributes.day,                    '0', 2),

            DAY_OF_WEEK : day_of_week.attributes.value,

            MONTH_STR   : this.attributes.month.attributes.name,
            DAY_OF_WEEK_STR : day_of_week.attributes.name,
        });
    },

    valueOf: function () {
        return this.time();
    },

}, {

    today: function () {
        return new Datetime.Date(new Date());
    },

});


Datetime.Time = Backbone.Model.extend({
    defaults: {
        hour:        0,
        minute:      0,
        second:      0,
        millisecond: 0,
    },

    constructor: function (data, options) {
        var opts = options || {};

        // Parse from number.
        if (_.isNumber(data)) {
            var date = new Date(data);
            data = opts.UTC ? {
                hour:        date.getUTCHours(),
                minute:      date.getUTCMinutes(),
                second:      date.getUTCSeconds(),
                millisecond: date.getUTCMilliseconds(),
            } : {
                hour:        date.getHours(),
                minute:      date.getMinutes(),
                second:      date.getSeconds(),
                millisecond: date.getMilliseconds(),
            };
        }

        // Parse from string.
        else if (_.isString(data)) {
            var tokens = str.split(':');
            var sec = parseFloat(tokens[2], 10);
            data = {
                hour:        parseInt(tokens[0], 10),
                minute:      parseInt(tokens[1], 10),
                second:      Math.round(sec),
                millisecond: Math.round(sec % 1 * 1000),
            };
        }

        // Parse from builtin Date().
        else if (data instanceof Date) {
            data = opts.UTC ? {
                hour:        data.getUTCHours(),
                minute:      data.getUTCMinutes(),
                second:      data.getUTCSeconds(),
                millisecond: data.getUTCMilliseconds(),
            } : {
                hour:        data.getHours(),
                minute:      data.getMinutes(),
                second:      data.getSeconds(),
                millisecond: data.getMilliseconds(),
            };
        }

        // Call parent constructor.
        this.__proto__.__proto__.constructor.apply(this, arguments);
    },

    initialize: function (attributes, options) {
        this.on('change:hour',        parse_int('hour'));
        this.on('change:minute',      parse_int('minute'));
        this.on('change:second',      parse_int('second'));
        this.on('change:millisecond', parse_int('millisecond'));

        if (attributes) {
            if (attributes.hour        !== undefined) parse_int('hour')        (this, attributes.hour);
            if (attributes.minute      !== undefined) parse_int('minute')      (this, attributes.minute);
            if (attributes.second      !== undefined) parse_int('second')      (this, attributes.second);
            if (attributes.millisecond !== undefined) parse_int('millisecond') (this, attributes.millisecond);
        }
    },

    hour: function () {
        return this.get('hour');
    },

    minute: function () {
        return this.get('minute');
    },

    second: function () {
        return this.get('second');
    },

    millisecond: function () {
        return this.get('millisecond');
    },

    to_string: function (format) {
        format = format || '%HOUR%:%MINUTE%:%SECOND%';
        return String.template_replace(format, {
            HOUR        : String.left_pad(this.attributes.hour,        '0', 2),
            MINUTE      : String.left_pad(this.attributes.minute,      '0', 2),
            SECOND      : String.left_pad(this.attributes.second,      '0', 2),
            MILLISECOND : String.left_pad(this.attributes.millisecond, '0', 6),
        });
    },

    // Milliseconds since 00:00:00
    valueOf: function () {
        return new Date(0).setUTCHours(
            this.attributes.hour,
            this.attributes.minute,
            this.attributes.second,
            this.attributes.millisecond
        ).valueOf();
    },
});


})();
