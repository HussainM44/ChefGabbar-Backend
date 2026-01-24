from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Variables

ROLE = (
    ("C","Customer"),
    ('M','Manager'),
    )

# User Auth

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="main_app/static/uploads", default="")
    role = models.CharField(max_length=2, choices=ROLE , default=[0][0])
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user} is a {self.role}'


