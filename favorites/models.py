from django.db import models
from users.models import User  # Import User model from users app
from movies.models import Movie  # Import Movie model from movies app

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.movie.title}"
