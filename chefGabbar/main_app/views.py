from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login
from .forms import profileForm, userUpdateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.


# BASIC Views


def home(request):
    return render(request, "home.html")


#  User Auth
# creating the profile and sign up in same def


def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        # importing form from forms.py & req.FILES for image uploading
        profile_form = profileForm(request.POST, request.FILES)
        # checking the form is valid or not
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # saving profile with user and profile model
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # logging in the same user
            login(request, user)
            return redirect("/")
        else:
            error_message = "Invalid sign up - try again"
    else:
        user_form = UserCreationForm()
        profile_form = profileForm()
        error_message = None
        # sending forms and error messages to the template
    return render(
        request,
        "registration/signup.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "error_message": error_message,
        },
    )


# User Profile views


class UserDetail(DetailView):
    model = User


def userUpdate(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user_id=user_id)

    if request.method == "POST":
        user_form = userUpdateForm(request.POST, instance=user)
        profile_form = profileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            login(request , user)
            return redirect("/")
        else:
            error_message = "Invalid Sign Up- TRY AGAIN"
    else:
        user_form = userUpdateForm(instance=user)
        profile_form = profileForm(instance=profile)
        error_message = None
    return render(
        request,
        "registration/userUpdate.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "error_message": error_message,
        },
    )
