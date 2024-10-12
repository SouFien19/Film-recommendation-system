from rest_framework import generics, permissions
from .models import Watchlist
from .serializers import WatchlistSerializer

class WatchlistCreateView(generics.CreateAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically associate with logged-in user

class WatchlistListView(generics.ListAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)  # Only show current user's watchlist
