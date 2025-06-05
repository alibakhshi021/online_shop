from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
    path('forget', views.ForgetView.as_view(), name='forget-pass'),
    path('reset_pass/<active_code>', views.ResetPasswordView.as_view(), name='reset-pass'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),
]
