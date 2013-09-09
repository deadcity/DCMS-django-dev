from django.conf.urls import patterns, url
from django.contrib.auth import views
from accounts import views as account_views


urlpatterns = patterns('',
    url(r'^login/$',  views.login,  {'template_name': 'accounts/login.html'},  name = 'login'),
    url(r'^logout/$', views.logout, {'template_name': 'accounts/logout.html'}, name = 'logout'),
    url(r'^register/$', account_views.register, name = 'register'),
    url(r'^profile/$', account_views.profile, name = 'profile'),
)
