from django.db import models

class User(models.Model):
    ROLE_CHOICES = [('admin', 'Admin'), ('user', 'User')]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField()
    genre = models.CharField(max_length=100)
    description = models.TextField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)