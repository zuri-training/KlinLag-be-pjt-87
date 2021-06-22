from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Users


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Enter Your First Name.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    phone = forms.CharField(max_length=11, required=True, help_text='Enter Nigerian Phone number')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    location = forms.CharField(max_length=300, help_text='Where do you live?')

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'location', 'password1', 'password2')


class AgencySignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Enter Your First Name.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    phone = forms.CharField(max_length=11, required=True, help_text='Enter Nigerian Phone number')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2')
