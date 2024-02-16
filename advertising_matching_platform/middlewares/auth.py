from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from django.http import JsonResponse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the current path is a public api
        if request.path in ["/api/auth/login", "/api/auth/register"]:
            # Allow access to public api
            return self.get_response(request)

        # Extract the access token from the Authorization header
        access_token = request.META.get("HTTP_AUTHORIZATION", "").split(" ")[1]

        # Use JWTAuthentication to decode and validate the access token
        jwt_authentication = JWTAuthentication()

        try:
            validated_token = jwt_authentication.get_validated_token(access_token)
        except InvalidToken:
            # Handle invalid token case if needed
            return JsonResponse({"error": "Invalid access token"}, status=401)

        # Retrieve the user and token objects from the validated token
        user = jwt_authentication.get_user(validated_token)

        # You can access the authenticated user if necessary
        request.user = user

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Unauthorized"}, status=401)

        # Check if the current path is an admin page
        if request.path.startswith("/api/admin/"):
            # Check if the user has admin authority
            if not request.user.is_superuser:
                return JsonResponse({"error": "Unauthorized"}, status=403)

        # Allow access to private and authorized api
        return self.get_response(request)
