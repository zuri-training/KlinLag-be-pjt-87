from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_giver = models.BooleanField(default=False)
    is_collector = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50,  help_text='Enter Your First Name.')
    last_name = models.CharField(max_length=50,  help_text='Optional.')
    phone = models.CharField(max_length=11, help_text='Enter Nigerian Phone number', unique=True)
    email = models.EmailField(max_length=254, help_text='Required. Enter a valid email address.', unique=True)
    location = models.CharField(max_length=300, help_text='Where do you live?')
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'email', 'location', 'is_giver', 'is_collector']
