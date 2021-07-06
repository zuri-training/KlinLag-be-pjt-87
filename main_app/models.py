from django.db import models
from django.contrib.auth.models import AbstractUser
from klin_api.models import User
from autoslug import AutoSlugField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    section_points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.first_name)


