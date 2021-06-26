from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from klin_api.models import User


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'location', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
            'first_name': None,
            'last_name': None,
            'phone': None,
            'email': None,
            'location': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Enter Password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),

        }

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
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
            'first_name': None,
            'last_name': None,
            'phone': None,
            'email': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Enter Password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_collector = True
        if commit:
            user.save()
        return user

