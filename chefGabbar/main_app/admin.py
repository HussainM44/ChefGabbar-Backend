from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile , Menu , Dish

# Register your models here.
admin.site.register(Profile)
admin.site.register(Menu)
admin.site.register(Dish)
