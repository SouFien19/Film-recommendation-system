# favorites/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet

router = DefaultRouter()
router.register('', FavoriteViewSet)

urlpatterns = [
    path('favorites/', include(router.urls)),
]
