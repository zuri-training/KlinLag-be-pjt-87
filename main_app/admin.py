from django.contrib import admin
 
from .models import User, SectionPoints
 
# Register your models here.
admin.site.register(User)
admin.site.register(SectionPoints)
 
from .models import User, Profile
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
 
