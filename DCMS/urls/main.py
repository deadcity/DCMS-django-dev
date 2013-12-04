from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView

# import traits

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

_urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DCMS.views.home', name='home'),
    # url(r'^DCMS/', include('DCMS.foo.urls')),

    url(r'^$', RedirectView.as_view(url = settings.URL_PREFIX + '/characters/')),

    url(r'^api/',        include('DCMS.urls.api')),
    url(r'^accounts/',   include('accounts.urls')),
    url(r'^characters/', include('character.urls.character_management')),
    url(r'^chronicles/', include('chronicle.urls.chronicle_management')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

_urlpatterns += staticfiles_urlpatterns()

if settings.URL_PREFIX is '':
    urlpatterns = _urlpatterns
else:
    url_prefix = settings.URL_PREFIX.strip('/') + '/'
    urlpatterns = patterns('', url(r'^' + url_prefix, include(_urlpatterns)))
