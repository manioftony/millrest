from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from serializers import ProfileSerializer
from models import Profile,Org
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.









class SnippetList(ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Org.objects.all()
    serializer_class = ProfileSerializer


class RestrictedView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        import ipdb;ipdb.set_trace()
        data = {
            'id': request.user.id,
            'username': request.user.username,
            'token': str(request.auth)
        }
        return Response(data)







