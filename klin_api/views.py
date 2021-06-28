from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, AgencySerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from djoser import views
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


class UserCreate(views.TokenCreateView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgencyCreate(views.TokenCreateView):
    def post(self, request, format ='json'):
        serializer = AgencySerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)