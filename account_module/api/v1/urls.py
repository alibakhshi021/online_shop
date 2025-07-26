from django.urls import path, include
from . import views
from .views import (RegistrationApiView, LoginAPIView, LogoutAPIView,
                     CustomTokenObtainPairView, ChangePassApiView, ProfileApiView, TestEmailView)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    #Register
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),

    path('test-email/', views.TestEmailView.as_view(), name='test_email'),
    
    #Login Token
    path('token/login/', LoginAPIView.as_view(), name='login'),
    path('token/logout/', LogoutAPIView.as_view(), name='logout'),
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    #change password
    path('change-password/', views.ChangePassApiView.as_view(), name='change-password'),
    path('profile/', views.ProfileApiView.as_view(), name='profile'),
    # path('accounts/', include('account_module.api.v1.urls.accounts')),
    # path('profile/', include('account_module.api.v1.urls.profile')),

 ]
