from django.urls import path
from controllers.authCtr import authCtr


urlpatterns = [
    path('auth/', authCtr.as_view(), name='auth'),
]