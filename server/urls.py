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
    ProjectsView,
    ProjectView,
    # ProjectSectionListView,
    # ClientProjectView,
    # UserProjectView,
)
from section.views import (
    SectionListView,
    SectionView,
    ProjectSectionView,
)  # , ClientSectionView, UserSectionView
from message.views import MessageView  # , ClientMessageView, UserMessageView
from payment.views import PaymentView
from advert.views import AdvertView

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
    path("api/project", ProjectsView.as_view(), name="projects"),
    path("api/project/<int:id>", ProjectView.as_view(), name="project"),
    path(
        "api/project/<int:project_id>/section",
        ProjectSectionView.as_view(),
        name="section",
    ),
    path("api/section/<int:id>", SectionView.as_view(), name="section"),
    path(
        "api/section/<int:section_id>/message", MessageView.as_view(), name="messages"
    ),
    path(
        "api/section/<int:section_id>/message/step/<int:step>",
        MessageView.as_view(),
        name="message",
    ),
    path("api/section/<int:section_id>/payment", PaymentView.as_view(), name="payment"),
    path("api/section/<int:section_id>/advert", AdvertView.as_view(), name="advert"),
    path(
        "api/section/step/<int:step_from>/<int:step_to>",
        SectionListView.as_view(),
        name="sections",
    ),
]
