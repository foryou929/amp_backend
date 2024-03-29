from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from auth.views import (
    RegisterView,
    LoginView,
    LoginWithTokenView,
    LogoutView,
    TokenRefreshView
)

from user.views import UserView, AvatarUploadView
from space.views import SpacesView, SpaceView
from project.views import (
    ProjectsView,
    ProjectView,
)
from section.views import (
    SectionsView,
    SectionView,
    SectionsProjectView,
    SectionsSpaceView,
)
from message.views import MessageView
from payment.views import SectionPaymentView, PaymentListView
from advert.views import AdvertView
from file.views import FileUploadView
from image.views import ImageUploadView
from review.views import ReviewView

urlpatterns = [
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/auth/register", RegisterView.as_view()),
    path("api/auth/login", LoginView.as_view()),
    path("api/auth/loginWithToken", LoginWithTokenView.as_view()),
    path("api/auth/logout", LogoutView.as_view()),
    path("api/<str:type>/<int:id>", UserView.as_view()),
    path("api/<str:type>/<int:id>/avatar", AvatarUploadView.as_view()),
    path("api/<str:type>/space", SpacesView.as_view()),
    path("api/<str:type>/space/<int:id>", SpaceView.as_view()),
    path("api/<str:type>/project", ProjectsView.as_view()),
    path("api/<str:type>/project/<int:id>", ProjectView.as_view()),
    path("api/<str:type>/section", SectionsView.as_view()),
    path("api/<str:type>/section/<int:id>", SectionView.as_view()),
    path("api/<str:type>/section/<int:section_id>/message", MessageView.as_view()),
    path("api/<str:type>/section/<int:section_id>/payment", SectionPaymentView.as_view()),
    path("api/<str:type>/section/<int:section_id>/advert", AdvertView.as_view()),
    path("api/<str:type>/section/<int:section_id>/review", ReviewView.as_view()),
    path("api/<str:type>/section/project/<int:project_id>", SectionsProjectView.as_view()),
    path("api/<str:type>/section/space/<int:space_id>", SectionsSpaceView.as_view()),
    path("api/<str:type>/message/<int:message_id>", FileUploadView.as_view()),
    path("api/<str:type>/payment", PaymentListView.as_view()),
    path("api/<str:mode>/image/<str:type>/<int:id>", ImageUploadView.as_view()),
]

urlpatterns += static("media", document_root=settings.MEDIA_ROOT)