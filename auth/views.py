from django.contrib.auth import authenticate, logout
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from auth.serializer import UserSerializer
from server.settings import SECRET_KEY
import jwt


class LoginView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)
                refresh_token = jwt.encode(refresh.payload, SECRET_KEY, algorithm='HS256')
                access_token = jwt.encode(access.payload, SECRET_KEY, algorithm='HS256')
                token = {
                    "refresh": refresh_token,
                    "access": access_token,
                }
                return Response({"message": "Login successful", "token": token})
            return Response({"error": "Invalid credentials"}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        

class RegisterView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful"}, status=201)
        return Response(serializer.errors, status=400)


class LoginWithTokenView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})


class TokenRefreshView(views.APIView):
    def post(self, request):
        refresh = RefreshToken(request.data["refresh"])
        access_token = jwt.encode(refresh.access_token.payload, SECRET_KEY, algorithm='HS256')
        return Response({"access": access_token})