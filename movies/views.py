# movies/views.py

from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admin users to perform CRUD operations.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()
