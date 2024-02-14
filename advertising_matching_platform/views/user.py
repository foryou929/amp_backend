from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from advertising_matching_platform.serializers.user import UserSerializer
from django.middleware.csrf import get_token


class RegisterView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful"}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({"csrf_token": get_token(request)})

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"})
        return Response({"message": "Invalid credentials"}, status=400)


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})
