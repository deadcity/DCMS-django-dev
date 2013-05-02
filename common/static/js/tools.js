(function () {

function create_namespace (namespace_name) {
    if (namespace_name === '') return window;

    var tokens = namespace_name.split('.');
    var parent = window;
    var tok = '';

    for (var i in tokens) {
        tok = tokens[i];
        parent[tok] = parent[tok] || {};
        parent = parent[tok];
    }

    return parent;
}

var Tools = create_namespace('Tools');
Tools.create_namespace = create_namespace;


// If 'prop' is a function, this will call that function on the specified
// object.  Otherwise it will just return the value of the property.
Tools.eval = function (object, prop) {
    return _.isFunction(object[prop]) ? object[prop]() : object[prop];
}

})();
