from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from musicapp.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicapp.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegistrationView.as_view(), name='register'),
]
