from functools import wraps
from urlparse import urlparse

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.encoding import force_str
from django.shortcuts import resolve_url

def user_passes_test(test_func, login_url = None, redirect_field_name = REDIRECT_FIELD_NAME, *args, **kwargs):
    """
    This is the excact same function decorator as django.contrib.auth.decorators.user_passes_test.
    The only difference is that this version forwards arbitrary arguments to the test function
    that were received in the decorator.
    """

    def decorator(view_func):
        @wraps(view_func, assigned = available_attrs(view_func))
        def _wrapped_view(request, *_args, **_kwargs):
            if test_func(request.user, *args, **kwargs):
                return view_func(request, *_args, **_kwargs)

            path = request.build_absolute_uri()
            # urlparse chokes on lazy objects in Python 3, force to str
            resolved_login_url = force_str(
                resolve_url(login_url or settings.LOGIN_URL))
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator
