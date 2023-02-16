from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    image = models.ImageField(default='default.png', upload_to='profile/images')