from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.views import (
    RegisterView,
    LoginView,
    LoginWithTokenView,
    LogoutView,
)

from user.views import ProfileView
from space.views import SpaceView
from project.views import (
    ProjectListView,
    ProjectView,
    ClientProjectView,
    UserProjectView,
)
from section.views import ClientView as ClientSectionView, UserView as UserSectionView
from message.views import ClientMessageView, UserMessageView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/register", RegisterView.as_view(), name="register"),
    path("api/auth/login", LoginView.as_view(), name="login"),
    path(
        "api/auth/loginWithToken", LoginWithTokenView.as_view(), name="loginWithToken"
    ),
    path("api/auth/logout", LogoutView.as_view(), name="logout"),
    path("api/user/profile", ProfileView.as_view(), name="profile"),
    path("api/space", SpaceView.as_view(), name="space"),
    path("api/project", ProjectListView.as_view(), name="project_kust"),
    path("api/project/<int:id>", ProjectView.as_view(), name="project"),
    path("api/client/project", ClientProjectView.as_view(), name="client_project"),
    path("api/user/project", UserProjectView.as_view(), name="user_project"),
    path(
        "api/user/section/<int:project_id>",
        UserSectionView.as_view(),
        name="user_section",
    ),
    # path("api/client/message/<int:section>", ClientMessageView.as_view(), name="client_message"),
    # path("api/user/message/<int:section>", UserMessageView.as_view(), name="user_message")
]
