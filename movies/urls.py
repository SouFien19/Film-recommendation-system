# users/urls.py
from django.db import router
from django.urls import include, path
from .views import MovieCreateView

urlpatterns = [
    path('users/', include(router.urls)),
    path('movies/add/', MovieCreateView.as_view(), name='add_movie'),  # Add this line
]
