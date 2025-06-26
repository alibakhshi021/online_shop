from django.urls import path, include
from . import views
from .views import RegistrationApiView, CustomAuthToken

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', views.CustomAuthToken.as_view(), name='token-login'),
    # path('login/', LoginAPIView.as_view(), name='login'),

 ]
