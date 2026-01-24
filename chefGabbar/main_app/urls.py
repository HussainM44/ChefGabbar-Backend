from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.home, name='home'),

    # User Auth
    path("accounts/signup/",views.signup , name='signup'),

    # User Profile
    path('profile/<int:pk>/', views.UserDetail.as_view(), name = "profile")

]
