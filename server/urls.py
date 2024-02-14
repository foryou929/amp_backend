from django.urls import path
from advertising_matching_platform.views.user import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('api/auth/register', RegisterView.as_view(), name='register'),
    path('api/auth/login', LoginView.as_view(), name='login'),
    path('api/auth/logout', LogoutView.as_view(), name='logout'),
]