from django.urls import path, include
from . import views

app_name = "product"
urlpatterns = [
    # path('', views.product_list, name='product-list'),
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("cat/<cat>", views.ProductListView.as_view(), name="product-category-list"),
    path("brand/<brand>", views.ProductListView.as_view(), name="product-brand-list"),
    path(
        "product-favorite", views.AddProductFavorite.as_view(), name="product-favorite"
    ),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product-details"),
    path("api/v1/", include("product_module.api.v1.urls")),
]
