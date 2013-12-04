from django.db import connection

from rest_framework import status
from rest_framework.response import Response

from common.context_managers import db_user


class DbUserMixin(object):
  def dispatch(self, request, *args, **kwargs):
    with db_user(connection, request.user.username):
      return super(DbUserMixin, self).dispatch(request, *args, **kwargs)


class HistoryMixin(object):
  """
  Overrides 'create' from 'mixins.CreateModelMixin' to allow creation of a
  record with a specific pk if it is specified.
  """
  def create(self, request, *args, **kwargs):
    if 'pk' in kwargs:
      record = self.model(id = int(kwargs['pk']))
    else:
      record = self.model()
    print request.DATA

    serializer = self.get_serializer(record, data = request.DATA, files = request.FILES)
    if serializer.is_valid():
      self.pre_save(serializer.object)
      self.object = serializer.save()
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status = status.HTTP_201_CREATED, headers = headers)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
