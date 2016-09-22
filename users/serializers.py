
from rest_framework import serializers

__author__ = 'kas'


class UserSerializer(serializers.Serializer):

    first_name = serializers.CharField()  # la variable debe tener mismo nombre del campo
    last_name = serializers.CharField()

