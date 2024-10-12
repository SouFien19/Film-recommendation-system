# authentication/urls.py

from django.urls import path
from .views import UserCreate, UserProfileDetail, CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('profile/<str:username>/', UserProfileDetail.as_view(), name='user-profile'),
    path('login/', CustomAuthToken.as_view(), name='login'),  # Token Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Authentication
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT
]