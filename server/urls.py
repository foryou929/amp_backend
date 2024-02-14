from django.urls import include, path

urlpatterns = [
    # Include the router URLs for users
    path('api/', include('routers.authRouter')),

    # Add more URL includes for other router files
]