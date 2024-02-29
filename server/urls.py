from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.views import (
    RegisterView,
    LoginView,
    LoginWithTokenView,
    LogoutView,
)

from user.views import UsersView, UserView
from space.views import SpaceView
from project.views import (
    ProjectsView,
    ProjectView,
)
from section.views import (
    SectionsView,
    SectionView,
    SectionProjectView,
)
from message.views import MessageView
from payment.views import PaymentView
from advert.views import AdvertView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/auth/register", RegisterView.as_view()),
    path("api/auth/login", LoginView.as_view()),
    path("api/auth/loginWithToken", LoginWithTokenView.as_view()),
    path("api/auth/logout", LogoutView.as_view()),
    path("api/user/<int:id>", UserView.as_view()),
    path("api/space", SpaceView.as_view()),
    path("api/project", ProjectsView.as_view()),
    path("api/project/<int:id>", ProjectView.as_view()),
    path("api/project/<str:type>", ProjectsView.as_view()),
    path("api/section/<int:id>", SectionView.as_view()),
    path("api/section/<str:type>", SectionsView.as_view()),
    path("api/section/<int:section_id>/message", MessageView.as_view()),
    path("api/section/<int:section_id>/payment", PaymentView.as_view()),
    path("api/section/<int:section_id>/advert", AdvertView.as_view()),
    path("api/section/project/<int:project_id>", SectionProjectView.as_view()),
]
