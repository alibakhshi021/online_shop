from django.urls import path, include
from . import views
from .views import RegistrationApiView, LoginAPIView, LogoutAPIView, CustomTokenObtainPairView, ChangePassApiView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', LoginAPIView.as_view(), name='login'),
    path('token/logout/', LogoutAPIView.as_view(), name='logout'),
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    path('change-password/', views.ChangePassApiView.as_view(), name='change-password')

 ]
