from django.urls import path
from . import views

app_name= 'api-v1'

urlpatterns = [
    # path('post/', views.ProductList.as_view(), name='product_list_api'),
    # path('post/<int:pk>/', views.ProductDetail.as_view(), name='product_detail_api'),
    path('post/', views.ProductListView.as_view({'get':'list'}), name='product_list'),
    path('post/<int:pk>/', views.ProductListView.as_view({'get':'retrieve'}), name='product_detail'),
    
]