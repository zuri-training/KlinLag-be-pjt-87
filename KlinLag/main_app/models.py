from django.db import models
from django.contrib.auth.models import AbstractUser
from klin_api.models import User
from django.contrib.gis.db import models

# Create your models here.


class SectionPoints(models.Model):
    appUser = models.ForeignKey(User, on_delete=models.CASCADE)
    pointsGained = models.IntegerField

    def __str__(self):
        return 'points'
