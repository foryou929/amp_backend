from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, logout
from auth.serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


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

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                token = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
                return Response({"message": "Login successful", "token": token})
            return Response({"error": "Invalid credentials"}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})


class ProfileView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.data)
        return Response({"message": "Success"})
