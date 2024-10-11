from django.contrib.auth.hashers import make_password
from django.db import models

class User(models.Model):
    ROLE_CHOICES = [('admin', 'Admin'), ('user', 'User')]
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Hash the password
        super().save(*args, **kwargs)