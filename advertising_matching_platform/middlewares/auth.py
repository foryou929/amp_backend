from django.shortcuts import redirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the current path is a public page
        print(request.path)
        if request.path in ['/api/auth/login', '/api/auth/register']:
            # Allow access to public pages
            return self.get_response(request)

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Redirect to the login page
            return redirect(reverse('login'))

        # Check if the current path is an admin page
        if request.path.startswith('/api/admin/'):
            # Check if the user has admin authority
            if not request.user.is_superuser:
                # Redirect to an unauthorized page or display an error message
                return redirect(reverse('unauthorized'))

        # Allow access to private and authorized pages
        return self.get_response(request)