from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index_page"),
    path("about/", views.AboutView.as_view(), name="about_page"),
    # path('site-partial', views.site_header_partial, name='site-partial'),
]
