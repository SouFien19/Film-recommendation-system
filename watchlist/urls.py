# watchlist/urls.py

from django.urls import path
from .views import WatchlistCreateView, WatchlistListView

urlpatterns = [
    path('watchlist/', WatchlistListView.as_view(), name='watchlist-list'),  # GET for list
    path('watchlist/create/', WatchlistCreateView.as_view(), name='watchlist-create'),  # POST for create
]
