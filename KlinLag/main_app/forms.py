from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from klin_api.models import User


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'location', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_giver = True
        if commit:
            user.save()
        return user


class AgencySignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_collector = True
        if commit:
            user.save()
        return user

