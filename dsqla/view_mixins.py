## @package dsqla.view_mixins
#  Mixin classes for views related to SQLAlchemy.


import json

from dsqla.models import get_model


## Parses request body as json and saves result to request.data.
#
#  This should only be mixed in to view classes that expect only a Content-Type
#  of "application/json".
class JsonBody (object):
    def dispatch (self, request, *args, **kwargs):
        if request.body:
            request.data = json.loads(request.body.decode('ascii'))
        else:
            request.data = None
        return super(JsonBody, self).dispatch(
            request, *args, **kwargs)


## Mixin to add Model class as a property to the host view based on view args.
#
class ModelView (object):
    @property
    def Model (self):
        if not hasattr(self, '_Model'):
            self._Model = get_model(self._module, self._model_name)
        return self._Model

    def dispatch (self, request, *args, **kwargs):
        self._module = kwargs.pop('module')
        self._model_name = kwargs.pop('model')
        return super(ModelView, self).dispatch(request, *args, **kwargs)
