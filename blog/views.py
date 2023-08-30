from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .serializer import CategorySerializer, PostSerializer, PostContentSerializer
from .models import Categories, Post
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostContentSerializer
        return PostSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
