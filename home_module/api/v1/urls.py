from django.urls import path
from . import views

app_name= 'api-v1'

urlpatterns = [
    path('', views.home_view, name='index_page1'),
    
]