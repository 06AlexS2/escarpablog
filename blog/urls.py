from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, PostView
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'categories', CategoryView, 'categories')
router.register(r'posts', PostView, 'posts')



urlpatterns = [
    path("blog/", include(router.urls)),
]