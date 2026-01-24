from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import profileForm
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic import ListView , DetailView

# Create your views here.


# BASIC Views


def home(request):
    return render(request, "home.html")

