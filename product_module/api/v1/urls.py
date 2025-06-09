from django.urls import path
from . import views

app_name= 'api-v1'

urlpatterns = [
    path('post/', views.product_view, name='product_api'),
    path('post/<int:id>/', views.detail_view, name='index_page2'),
    
]