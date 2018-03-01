from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_auth.views import LogoutView


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))


class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)
