from django.urls import path
from . import views

# app_name = "index_page"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index_page"),
    path("about/", views.AboutView.as_view(), name="about_page"),
    # path('site-partial', views.site_header_partial, name='site-partial'),
]
