from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

# forms here
class profileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['image','role', 'address']

class userUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']
