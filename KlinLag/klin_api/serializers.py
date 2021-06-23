from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import User
from django.db import transaction
from rest_framework.validators import UniqueValidator


class UserSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'location',
                  'password']



class AgencySerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'password'
                  ]