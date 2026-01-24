from django.forms import ModelForm
from .models import Profile

# forms here
class profileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['image','role', 'address']
