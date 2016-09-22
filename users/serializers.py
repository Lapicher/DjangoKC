from django.contrib.auth.models import User
from rest_framework import serializers

__author__ = 'kas'


class UserSerializer(serializers.Serializer):

    first_name = serializers.CharField()  # la variable debe tener mismo nombre del campo
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.password = validated_data.get('password')
        instance.email = validated_data.get('email')
        instance.save()
        return instance



