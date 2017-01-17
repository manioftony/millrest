from rest_framework import generics as g
from serializers import model_serializer_factory
from common_methods import auto_as_view
from django.apps import apps
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import JsonResponse


class JsonManager(object):
    permission_classes = (AllowAny,)
    def dispatch(self, *args, **kwargs):
        return super(JsonManager, self).dispatch(*args, **kwargs)

    def get_mdl(self):
        # return get_model('crm', self.kwargs.get('model'))
        # import ipdb;ipdb.set_trace()
        if self.kwargs.get('model')=='user':
            return apps.get_model(app_label='auth', model_name='User')
        return apps.get_model(app_label='masterdata', model_name=self.kwargs.get('model'))

    def get_queryset(self):
        # import ipdb;ipdb.set_trace()
        mdl = self.get_mdl()
        return mdl.objects.all()

    def get_serializer_class(self):
        return model_serializer_factory(self.get_mdl())

    def get_object(self):
        qs = self.get_queryset()
        return qs.get(id=self.kwargs.get('object_id'))


@auto_as_view
class ListCFeed(JsonManager, g.ListAPIView):

    pass


@auto_as_view
class AddCFeed(JsonManager, g.CreateAPIView):

    pass


@auto_as_view
class EditCFeed(JsonManager, g.UpdateAPIView):

    def post(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)


@auto_as_view
class ActiveCFeed(JsonManager, g.DestroyAPIView):

    def perform_destroy(self, instance):
        # import ipdb;ipdb.set_trace()
        instance.active = {0: 2, 2: 0}[instance.active]
        self.message = '%s %s successfully' % (
            self.kwargs.get('model'),
            {2: 'activated', 0: 'deactivated'}[instance.active])
        self.status = {2: 'True', 0: 'False'}[instance.active]
        instance.save()

    def delete(self, request, *args, **kwargs):
        super(ActiveCFeed._original, self).delete(request, *args, **kwargs)
        return JsonResponse({"data":self.message,"status":self.status})