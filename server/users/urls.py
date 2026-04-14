from django.urls import path
from .views import RegisterView, UserProfileView, register_user
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('profile/<int:user_id>/', UserProfileView.as_view()),
    path('register/', register_user),
    
]