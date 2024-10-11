# movies/urls.py

from django.urls import path
from .views import UserViewSet, MovieViewSet, WatchlistViewSet, FavoriteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('watchlist', WatchlistViewSet)
router.register('favorites', FavoriteViewSet)

urlpatterns = router.urls
