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
from file.views import FileUploadView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/auth/register", RegisterView.as_view()),
    path("api/auth/login", LoginView.as_view()),
    path("api/auth/loginWithToken", LoginWithTokenView.as_view()),
    path("api/auth/logout", LogoutView.as_view()),
    path("api/<str:type>/<int:id>", UserView.as_view()),
    path("api/<str:type>/space", SpaceView.as_view()),
    path("api/<str:type>/project", ProjectsView.as_view()),
    path("api/<str:type>/project/<int:id>", ProjectView.as_view()),
    path("api/<str:type>/section", SectionsView.as_view()),
    path("api/<str:type>/section/<int:id>", SectionView.as_view()),
    path("api/<str:type>/section/<int:section_id>/message", MessageView.as_view()),
    path("api/<str:type>/section/<int:section_id>/payment", PaymentView.as_view()),
    path("api/<str:type>/section/<int:section_id>/advert", AdvertView.as_view()),
    path("api/<str:type>/section/project/<int:project_id>", SectionProjectView.as_view()),
    path("api/upload", FileUploadView.as_view())
]
