from django.conf.urls import patterns, url
from django.contrib.auth import views
from accounts import views as accounts_views


urlpatterns = patterns('',
    url(r'^login/$',  views.login,  {'template_name': 'accounts/login.html'},  name = 'login'),
    url(r'^logout/$', views.logout, {'template_name': 'accounts/logout.html'}, name = 'logout'),
    url(r'^register/$', accounts_views.register, name = 'register'),
    url(r'^profile/$', accounts_views.profile, name = 'profile'),
)
