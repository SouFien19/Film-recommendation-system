# watchlist/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WatchlistViewSet

router = DefaultRouter()
router.register('', WatchlistViewSet)

urlpatterns = [
    path('watchlist/', include(router.urls)),
]
