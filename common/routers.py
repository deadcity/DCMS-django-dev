import itertools

from rest_framework.compat import url
from rest_framework.routers import DefaultRouter, Route, SimpleRouter


def _replace_methodname(format_string, url_subpath, methodnamehyphen):
    ret = format_string
    ret = ret.replace('{url_subpath}',      url_subpath)
    ret = ret.replace('{methodnamehyphen}', methodnamehyphen)
    return ret

def _flatten(list_of_fields):
    return itertools.chain(*list_of_fields)

def _route_method(bind_type, methods, url_subpath, kwargs):
    def decorator(func):
        func.bind_type       = bind_type
        func.bind_to_methods = methods
        func.url_subpath     = url_subpath
        func.kwargs          = kwargs
        return func
    return decorator


def link(url_subpath = None, **kwargs):
    return _route_method('link', ['get'], url_subpath, kwargs)


def action(methods = ['post'], url_subpath = None, **kwargs):
    return _route_method('action', methods, url_subpath, kwargs)


def list_link(url_subpath = None, **kwargs):
    return _route_method('list-link', ['get'], url_subpath, kwargs)


def list_action(methods = ['post'], url_subpath = None, **kwargs):
    return _route_method('list-action', methods, url_subpath, kwargs)


class _RouteMixin_Metaclass(type):
    def __new__(mtcls, name, bases, attrs):
        # merge routes
        routes = []
        for base in bases:
            if hasattr(base, 'routes'):
                routes = routes + base.routes.items()

        if 'routes' in attrs:
            route_keys = attrs['routes'].keys()
            attrs['routes'] = dict(routes + attrs['routes'].items())
        else:
            route_keys = []
            attrs['routes'] = dict(routes)

        # merge route functions
        generate_routes = []
        for base in bases:
            if hasattr(base, '_generate_routes'):
                generate_routes = generate_routes + base._generate_routes.items()

        if 'generate_routes' in attrs:
            for key in route_keys:
                generate_routes.append((key, attrs['generate_routes']))
        attrs['_generate_routes'] = dict(generate_routes)

        return super(_RouteMixin_Metaclass, mtcls).__new__(mtcls, name, bases, attrs)


class BaseRouter(SimpleRouter):
    routes = {}

    def get_lookup_regex(self, viewset):
        """
        Given a viewset, return the portion of the URL regex that is used
        to match against a single instance.
        """
        base_regex = r'(?P<{lookup_field}>{lookup_pattern})'
        return base_regex.format(
            lookup_field = getattr(viewset, 'lookup_field', 'pk'),
            lookup_pattern = getattr(
                viewset,
                'lookup_pattern',
                '[^/]+' if self.trailing_slash else '[^/.]+'
            )
        )

    def get_routes(self, viewset):
        ret = []

        for key, route in self.routes.items():
            if key in self._generate_routes:
                ret.extend(self._generate_routes[key](self, key, viewset))
            else:
                ret.append(route)

        return ret

    def get_urls(self):
        """
        Override rest_framework.routers.SimpleRouter.get_urls to not break on
        certain regex syntax.
        """
        ret = []

        for prefix, viewset, basename in self.registry:
            lookup = self.get_lookup_regex(viewset)
            routes = self.get_routes(viewset)

            for route in routes:
                # Only actions which actually exist on the viewset will be bound.
                mapping = self.get_method_map(viewset, route.mapping)
                if not mapping: continue

                # Build the url pattern.
                regex = route.url
                regex = regex.replace('{prefix}',         prefix)
                regex = regex.replace('{lookup}',         lookup)
                regex = regex.replace('{trailing_slash}', self.trailing_slash)

                view = viewset.as_view(mapping, **route.initkwargs)
                name = route.name.format(basename = basename)
                ret.append(url(regex, view, name = name))

        return ret


class BaseRouteMixin(object):
    __metaclass__ = _RouteMixin_Metaclass


class ListRouteMixin(BaseRouteMixin):
    routes = {
        'list': Route(
            url        = r'^{prefix}{trailing_slash}$',
            mapping    = {
                'get'  : 'list',
                'post' : 'create',
            },
            name       = '{basename}-list',
            initkwargs = { 'suffix': 'List' }
        )
    }


class BatchUpdateListRouteMixin(BaseRouteMixin):
    routes = {
        'batch-update': Route(
            url        = r'^{prefix}{trailing_slash}$',
            mapping    = {
                'get'  : 'list',
                'put'  : 'batch_update',
                'post' : 'create',
            },
            name       = '{basename}-list',
            initkwargs = { 'suffix': 'List' }
        )
    }


class DetailRouteMixin(BaseRouteMixin):
    routes = {
        'detail': Route(
            url        = r'^{prefix}/{lookup}{trailing_slash}$',
            mapping    = {
                'get'    : 'retrieve',
                'put'    : 'update',
                'patch'  : 'partial_update',
                'delete' : 'destroy',
            },
            name       = '{basename}-detail',
            initkwargs = { 'suffix': 'Instance' }
        )
    }


def _get_dynamic_routes(viewset):
    dynamic_routes = getattr(viewset, '_dynamic_routes', None)
    if dynamic_routes:
        return dynamic_routes

    dynamic_routes = {}
    for membername in dir(viewset):
        member = getattr(viewset, membername)
        bind_type = getattr(member, 'bind_type', None)
        if bind_type:
            httpmethods = [method.lower() for method in member.bind_to_methods]
            if bind_type in dynamic_routes:
                routes = dynamic_routes[bind_type]
            else:
                routes = []
                dynamic_routes[bind_type] = routes
            routes.append((httpmethods, membername))

    setattr(viewset, '_dynamic_routes', dynamic_routes)
    return dynamic_routes


def _parse_dynamic_routes(viewset, route, dynamic_routes):
    ret = []
    for httpmethods, methodname in dynamic_routes:
        method = getattr(viewset, methodname)
        initkwargs = route.initkwargs.copy()
        initkwargs.update(method.kwargs)
        url_subpath = getattr(method, 'url_subpath', methodname)
        if not url_subpath:
            url_subpath = methodname
        methodnamehyphen = methodname.replace('_', '-')
        ret.append(Route(
            url        = _replace_methodname(route.url,  url_subpath, methodnamehyphen),
            mapping    = { httpmethod: methodname for httpmethod in httpmethods },
            name       = _replace_methodname(route.name, url_subpath, methodnamehyphen),
            initkwargs = initkwargs
        ))
    return ret


class DynamicDetailRouteMixin(BaseRouteMixin):
    routes = {
        'dynamic-detail': Route(
            url        = r'^{prefix}/{lookup}/{url_subpath}{trailing_slash}$',
            mapping    = None,  # Determined when route is constructed.
            name       = '{basename}-{methodnamehyphen}',
            initkwargs = {}
        )
    }

    def generate_routes(self, key, viewset):
        dynamic_routes = _get_dynamic_routes(viewset)
        ret = []

        if 'link' in dynamic_routes:
            ret.extend(_parse_dynamic_routes(
                viewset        = viewset,
                route          = self.routes['dynamic-detail'],
                dynamic_routes = dynamic_routes['link']
            ))

        if 'action' in dynamic_routes:
            ret.extend(_parse_dynamic_routes(
                viewset        = viewset,
                route          = self.routes['dynamic-detail'],
                dynamic_routes = dynamic_routes['action']
            ))

        return ret


class DynamicListRouteMixin(BaseRouteMixin):
    routes = {
        'dynamic-list': Route(
            url        = r'^{prefix}/{url_subpath}{trailing_slash}$',
            mapping    = None,  # Determined when route is constructed.
            name       = '{basename}-{methodnamehyphen}',
            initkwargs = {}
        )
    }

    def generate_routes(self, key, viewset):
        dynamic_routes = _get_dynamic_routes(viewset)
        ret = []

        if 'list-link' in dynamic_routes:
            ret.extend(_parse_dynamic_routes(
                viewset        = viewset,
                route          = self.routes['dynamic-list'],
                dynamic_routes = dynamic_routes['list-link']
            ))

        if 'list-action' in dynamic_routes:
            ret.extend(_parse_dynamic_routes(
                viewset        = viewset,
                route          = self.routes['dynamic-list'],
                dynamic_routes = dynamic_routes['list-action']
            ))

        return ret


class FullRouter(DetailRouteMixin,
                 BatchUpdateListRouteMixin,
                 DynamicDetailRouteMixin,
                 DynamicListRouteMixin,
                 BaseRouter):
    pass
