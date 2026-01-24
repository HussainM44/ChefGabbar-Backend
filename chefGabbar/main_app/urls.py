from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.home, name='home'),

]
