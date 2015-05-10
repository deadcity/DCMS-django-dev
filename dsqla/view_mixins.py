## @package dsqla.view_mixins
#  Mixin classes for views related to SQLAlchemy.


import json

from django_sqla.models import get_model


## Parses request body as json and saves result to request.data.
#
#  This should only be mixed in to view classes that exect only a Content-Type
#  of "application/json".
class JsonBody (object):
    def dispatch (self, request, *args, **kwargs):
        if request.body:
            request.data = json.loads(request.body)
        else:
            request.data = None
        return super(JsonBody, self).dispatch(
            request, *args, **kwargs)


## Mixin to add Model class to view based on view args.
#
class ModelView (object):
    @property
    def Model (self):
        if not hasattr(self, '_Model'):
            self._Model = get_model(self._schema, self._model_name)
        return self._Model

    def dispatch (self, request, *args, **kwargs):
        self._schema = kwargs.pop('schema')
        self._model_name = kwargs.pop('model')
        return super(ModelView, self).dispatch(request, *args, **kwargs)
