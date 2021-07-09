from django.contrib import admin

 
from .models import User, Profile, Blogpost, Comment, Schedule
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Blogpost)
admin.site.register(Comment)
admin.site.register(Schedule)
