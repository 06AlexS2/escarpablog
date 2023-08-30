from rest_framework import generics, permissions
from .models import User
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password


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
