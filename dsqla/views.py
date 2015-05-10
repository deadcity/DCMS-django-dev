## @package dsqla.views
#  View classes to handle direct database interactions.


from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from dsqla.models import ModelEncoder
from dsqla.session import session
from dsqla.view_mixins import JsonBody, ModelView


class InstanceView (JsonBody, ModelView, View):
    def dispatch (self, request, id, *args, **kwargs):
        self._id = int(id)
        return super(InstanceView, self).dispatch(request, *args, **kwargs)

    @property
    def model (self):
        if not hasattr(self, '_model'):
            self._model = session.query(self.Model).get(self._id)
        return self._model

    # CRUD: read
    def get (self, request):
        return JsonResponse(self.model.to_dict(), encoder = ModelEncoder)

    # CRUD: update
    def put (self, request):
        return self.patch(request)

    # CRUD: patch
    def patch (self, request):
        for fieldname, value in request.data.items():
            setattr(self.model, fieldname, value)
        session.commit()
        return self.get(request)

    # CRUD: delete
    def delete (self, request):
        session.delete(self.model)
        session.commit()
        return HttpRequest(content_type = 'application/json')


class CollectionView (JsonBody, ModelView, View):
    # CRUD: create
    def post (self, request):
        model = self.Model(**request.data)
        session.add(model)
        session.commit()
        return JsonResponse(model.to_dict(), encoder = ModelEncoder)

    # CRUD: read
    def get (self, request):
        return JsonResponse(
            [model.to_dict() for model in session.query(self.Model)],
            encoder = ModelEncoder,
            safe = False
        )
