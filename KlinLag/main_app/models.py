from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Users(AbstractUser):
    is_giver = models.BooleanField(default=False)
    is_collector = models.BooleanField(default=False)

class SectionPoints(models.Model):
    appUser = models.ForeignKey(Users, on_delete=models.CASCADE)
    pointsGained = models.IntegerField

    def __str__(self):
        return 'points'
