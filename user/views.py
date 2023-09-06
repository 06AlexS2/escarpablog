from rest_framework import generics, permissions
from .models import User
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.middleware import csrf
from datetime import datetime, timedelta





class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    def perform_create(self, serializer):
        # Hash de la contraseña antes de guardarla
        password = make_password(serializer.validated_data['password'])
        serializer.save(password=password)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            token = response.data['access']
            response = Response(response.data, status=response.status_code)
            response.set_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'], token, httponly=True, secure=True, samesite='Lax')
            csrf.get_token(request)
        return response

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = HttpResponse("deleted successfully.")
        
        if 'access_token' in request.COOKIES:
            response.delete_cookie('access_token')
        return response
    
class UserDataView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            # Aquí puedes acceder a los datos del usuario, como user.username, user.email, etc.
            return Response({"username": user.username, "email": user.email, "id": user.id, "name": user.name, "role": user.role})
        else:
            return Response({"message": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)
