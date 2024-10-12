from django.urls import path
from .views import UserCreate, UserProfileDetail

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('profile/<str:username>/', UserProfileDetail.as_view(), name='user-profile'),
]