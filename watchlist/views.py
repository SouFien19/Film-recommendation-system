from rest_framework import viewsets
from .models import Watchlist
from .serializers import WatchlistSerializer

class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer