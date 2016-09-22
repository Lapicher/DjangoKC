
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework.renderers import JSONRenderer

from users.serializers import UserSerializer

__author__ = 'kas'


class UserListAPI(View):
    """
    Endpoint de listado de usuarios
    """

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        render = JSONRenderer()
        data = render.render(serializer.data)
        return HttpResponse(data)
