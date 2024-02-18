from django.urls import path
from auth.views import (
    RegisterView,
    LoginView,
    LogoutView,
)

from user.views import ProfileView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/register", RegisterView.as_view(), name="register"),
    path("api/auth/login", LoginView.as_view(), name="login"),
    path("api/auth/logout", LogoutView.as_view(), name="logout"),
    path("api/user/profile", ProfileView.as_view(), name="profile"),
]
