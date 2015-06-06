## @module DCMS.urls.main
#  Main urls for DCMS project.


from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

# import traits


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


_urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DCMS.views.home', name='home'),
    # url(r'^DCMS/', include('DCMS.foo.urls')),

    url(r'^$', RedirectView.as_view(url = reverse_lazy('character-list'), permanent = True)),

    # url(r'^api/',        include('DCMS.urls.api')),
    url(r'^accounts/',   include('accounts.urls')),
    url(r'^characters/', include('characters.urls')),
    # url(r'^chronicles/', include('chronicles.urls')),
    url(r'^rest/',       include('dsqla.rest_urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

_urlpatterns += staticfiles_urlpatterns()

if settings.URL_PREFIX is '':
    urlpatterns = _urlpatterns
else:
    url_prefix = settings.URL_PREFIX.strip('/') + '/'
    urlpatterns = patterns('', url(r'^' + url_prefix, include(_urlpatterns)))
