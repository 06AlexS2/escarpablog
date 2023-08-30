from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[('reader', 'Reader'), ('admin', 'Admin')])
    is_verified = models.BooleanField(default=False)
    joinedAt = models.DateTimeField(auto_now_add=True)
