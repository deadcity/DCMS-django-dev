from django.conf.urls import patterns, url
from django.contrib.auth import views
from auth import views as auth_views


urlpatterns = patterns('',
    url(r'^login/$',  views.login,  {'template_name': 'auth/login.html'},  name = 'login'),
    url(r'^logout/$', views.logout, {'template_name': 'auth/logout.html'}, name = 'logout'),
    url(r'^register/$', auth_views.register, name = 'register'),
    url(r'^profile/$', auth_views.profile, name = 'profile'),
)
