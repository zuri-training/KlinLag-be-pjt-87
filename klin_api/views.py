from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from djoser import views
<<<<<<< HEAD:KlinLag/klin_api/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse_lazy

from django.views.generic.list import ListView
from .utils import Calendar
from .models import Schedule
=======
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from main_app.models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
>>>>>>> 4de1a8b31cd0ca5f548c0071f691321f44e5f90d:klin_api/views.py

# Create your views here.


class UserCreate(views.TokenCreateView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Profile.objects.create(user=user)
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
            Profile.objects.create(user=user)
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


<<<<<<< HEAD:KlinLag/klin_api/views.py
class CalendarView(ListView):
    model = Schedule
    template_name = 'components/calendar.html'
    success_url = reverse_lazy("calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = get_date(self.request.GET.get('month', None))
        cal = Calendar(date.year, date.month)
        html_cal = calendar.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context[prev_month] = prev_month(date)
        context[next_month] = next_month(date)

        return context
=======
class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileUpdateSerializer

    def get_object(self):
        return self.request.user.profile

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


>>>>>>> 4de1a8b31cd0ca5f548c0071f691321f44e5f90d:klin_api/views.py
