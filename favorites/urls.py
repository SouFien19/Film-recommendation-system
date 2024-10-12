# favorites/urls.py

from django.urls import path
from .views import FavoriteCreateView, FavoriteListView

urlpatterns = [
    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),  # GET for list
    path('favorites/create/', FavoriteCreateView.as_view(), name='favorite-create'),  # POST for create
]
