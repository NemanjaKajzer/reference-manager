from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Reference
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password' : {'write_only' : True, 'required' : True}}

    @permission_classes((AllowAny,))
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'title', 'someNumber']
