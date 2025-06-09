from django.urls import path
from . import views

app_name= 'api-v1'

urlpatterns = [
    path('post/', views.ProductList.as_view(), name='product_list_api'),
    path('post/<int:id>/', views.ProductDetail.as_view(), name='product_detail_api'),
    
]