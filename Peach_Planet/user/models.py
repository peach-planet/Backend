from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
     user_id = models.CharField(max_length=30, unique=True)
     nickname = models.CharField(max_length=300, unique=True)
     
     USERNAME_FIELD = 'user_id'
     REQUIRED_FIELDS = ['nickname']

