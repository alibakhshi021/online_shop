from rest_framework.permissions import AllowAny
from .serializers import ProductSerializers, CategorySerializer
from ...models import Product, ProductCategory
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination

# class ProductList(ListCreateAPIView):
#     """getting a list of post and creating new posts"""
#     permission_classes = [IsAuthenticated]
#     serializer_class = ProductSerializers
#     queryset = Product.objects.filter(is_active=True)


# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     """getting of the posts and edit plus removing it"""
#     permission_classes = [AllowAny]
#     serializer_class = ProductSerializers
#     queryset = Product.objects.filter(is_active=True)


class ProductModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, IsOwnerOrReadOnly]
    serializer_class = ProductSerializers
    queryset = Product.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact"],
        "brand": ["exact"],
        "is_active": ["exact"],
    }
    search_fields = ["title"]
    ordering_fields = ["price"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.filter(is_active=True)
