from django.db import models
from django.contrib.auth.models import AbstractUser
from klin_api.models import User
from autoslug import AutoSlugField
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    section_points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.first_name)


class Blogpost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blogpost,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

