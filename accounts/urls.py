from django.conf.urls import patterns, url
from django.contrib.auth import views


urlpatterns = patterns('',
    url(r'^login/$',  views.login,  {'template_name': 'accounts/login.html'},  name = 'login'),
    url(r'^logout/$', views.logout, {'template_name': 'accounts/logout.html'}, name = 'logout'),
)
