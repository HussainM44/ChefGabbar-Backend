from django.forms import ModelForm
from .models import Profile , Menu , Dish
from django.contrib.auth.models import User


# forms here
class profileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "role", "address"]


class userUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class menuCreateForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['cuisine']

class dishCreateForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name','description', 'dish_image']
