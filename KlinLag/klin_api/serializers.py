from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import User
from django.db import transaction
from rest_framework.validators import UniqueValidator


class UserSerializer(UserCreateSerializer):
    is_giver = serializers.BooleanField(default=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'location',
                  'password', 'is_giver', 'is_collector']


class AgencySerializer(UserCreateSerializer):
    is_collector = serializers.BooleanField(default=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'password', 'is_collector', 'is_giver'
                  ]