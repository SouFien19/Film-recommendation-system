from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),  # Auth routes
    path('api/', include('users.urls')),  # User API routes
    path('api/', include('movies.urls')),
    path('api/', include('watchlist.urls')),  # Watchlist API routes
    path('api/', include('favorites.urls')),  # Favorite API routes
]
