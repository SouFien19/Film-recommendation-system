# authentication/views.py
from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.permissions import IsAuthenticated

class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can add movies

