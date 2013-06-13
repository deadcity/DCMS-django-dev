from django.conf.urls import patterns, url

from chronicle.views import chronicle_management as views


urlpatterns = patterns('chronicle.views.chronicle_management',
    url(r'^$',             views.ChronicleListView.as_view(),   name = 'chronicle_list'),
    url(r'^(?P<pk>\d+)/$', views.ChronicleDetailView.as_view(), name = 'chronicle_detail'),
)
