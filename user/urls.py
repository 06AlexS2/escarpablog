from django.urls import path
from .views import CreateUserView, UserListView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from rest_framework import routers
from .views import UserListView, UserDetailView, UserDataView, CreateUserView, CustomTokenObtainPairView, LogoutView
from rest_framework.documentation import include_docs_urls

#api versioning
router = routers.DefaultRouter()

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/profile/', UserDataView.as_view(), name='user-profile'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('docs/users/', include_docs_urls("Users API"))
]
