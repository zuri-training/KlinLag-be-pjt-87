from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django.urls import reverse


class Schedule(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return self.title
    @property
    def get_calendar_url(self):
        url = reverse('schedule_edit', args=(self.id,))
        return f'<p>{self.title}</p><a href="{url}">edit</a>'


# Create your models here.
class User(AbstractUser):
    is_giver = models.BooleanField(default=False)
    is_collector = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, verbose_name=None)
    last_name = models.CharField(max_length=50, verbose_name=None)
    phone = PhoneNumberField(null=False, blank=False,  unique=True, verbose_name=None)
    email = models.EmailField(max_length=254,  unique=True, verbose_name=None)
    location = models.CharField(max_length=300, verbose_name=None)
    signup_confirmation = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
