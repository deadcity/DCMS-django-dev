## @package dsqla.rest_urls
#  Django URL mappings for SQLAlchemy REST views.


from django.conf.urls import url

from dsqla.views import CollectionView, InstanceView


urlpatterns = [
    url(r'^(?P<module>\w+)/(?P<model>\w+)$',             CollectionView.as_view(), name = 'dsqla-rest-collection'),
    url(r'^(?P<module>\w+)/(?P<model>\w+)/(?P<id>\d+)$', InstanceView.as_view(),   name = 'dsqla-rest-instance')
]
